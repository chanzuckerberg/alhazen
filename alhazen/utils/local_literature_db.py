# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/35_localdb.ipynb.

# %% auto 0
__all__ = ['read_information_content_entity_iri', 'get_nxml_from_pubmed_doi', 'download_file', 'get_pdf_from_pubmed_doi',
           'QuerySpec', 'LocalLiteratureDb']

# %% ../../nbs/35_localdb.ipynb 4
import local_resources.linkml as linkml

from .airtableUtils import AirtableUtils
from .searchEngineUtils import ESearchQuery, EuroPMCQuery
from .queryTranslator import QueryTranslator, QueryType
from ..schema_sqla import ScientificKnowledgeCollection, \
    ScientificKnowledgeExpression, ScientificKnowledgeCollectionHasMembers, \
    ScientificKnowledgeItem, ScientificKnowledgeExpressionHasRepresentation, \
    ScientificKnowledgeFragment, ScientificKnowledgeItemHasPart, \
    InformationResource, Note, NoteIsAbout
import alhazen.schema_python as linkml_py
from .jats_text_extractor import NxmlDoc

from bs4 import BeautifulSoup,Tag,Comment,NavigableString
from dataclasses import dataclass, field
from datetime import datetime
from importlib_resources import files
import local_resources.linkml as linkml
import os
import pandas as pd
from pathlib import Path
import re
import requests
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
import sqlite3  
import sys
from time import time,sleep
from tqdm import tqdm
from urllib.request import urlopen
from urllib.parse import quote_plus, quote, unquote
from urllib.error import URLError, HTTPError
import yaml
import uuid

# %% ../../nbs/35_localdb.ipynb 7
def read_information_content_entity_iri(ice, id_prefix):
    """Reads an identifier for a given prefix"""
    idmap = {k[:k.find(':')]:k[k.find(':')+1:] for k in ice.xref} 
    return idmap.get(id_prefix)

def get_nxml_from_pubmed_doi(doi, base_file_path):    
    """
    Executes a query on the target database and returns a count of papers 
    """
    if os.environ.get('NCBI_API_KEY') is None:
        raise Exception('Error attempting to query NCBI for URL data, did you set the NCBI_API_KEY environment variable?')
    api_key = os.environ.get('NCBI_API_KEY')

    esearch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?api_key='+api_key+'&db=pmc&term='+doi+'[doi]&retmode=xml'
    sleep(0.1)
    print(esearch_url)
    esearch_response = urlopen(esearch_url)
    esearch_data = esearch_response.read().decode('utf-8')
    esearch_soup = BeautifulSoup(esearch_data, "lxml-xml")
    id_tag = esearch_soup.find('Id')    
    if id_tag is None:
      print('No paper found with that DOI')
      return
      # raise Exception('Could not find "' + doi + '" in PMC')
    pmc_id = id_tag.string
    
    efetch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?api_key='+api_key+'&db=pmc&id='+pmc_id+'&retmode=xml'
    sleep(0.1)
    print(efetch_url)
    efetch_response = urlopen(efetch_url)
    efetch_data = efetch_response.read().decode('utf-8')
    xml = BeautifulSoup(efetch_data, "lxml-xml")
    body_tag = xml.findAll('body')
    if body_tag is None:
        return    
    
    file_path = Path(base_file_path + '/' + doi + '.nxml')
    parent_dir = file_path.parent
    if os.path.exists(parent_dir) is False:
        os.makedirs(parent_dir)
    with open(file_path, 'w') as f:
        f.write(str(xml))

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

def get_pdf_from_pubmed_doi(doi, base_file_path):    
    """
    Executes a query on the target database and returns a count of papers 
    """
    if os.environ.get('NCBI_API_KEY') is None:
        raise Exception('Error attempting to query NCBI for URL data, did you set the NCBI_API_KEY environment variable?')
    api_key = os.environ.get('NCBI_API_KEY')

    esearch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?api_key='+api_key+'&db=pmc&term='+doi+'[doi]&retmode=xml'
    sleep(0.1)
    print(esearch_url)
    esearch_response = urlopen(esearch_url)
    esearch_data = esearch_response.read().decode('utf-8')
    esearch_soup = BeautifulSoup(esearch_data, "lxml-xml")
    id_tag = esearch_soup.find('Id')    
    if id_tag is None:
      print('No paper found with that DOI')
      return
      # raise Exception('Could not find "' + doi + '" in PMC')
    pmc_id = id_tag.string

    # OA Dataset 
    oapi_url = 'https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id='+pmc_id+'&format=pdf'
    sleep(0.1)
    print(oapi_url)
    oapi_response = urlopen(oapi_url)
    oapi_data = oapi_response.read().decode('utf-8')    
    oapi_soup = BeautifulSoup(oapi_data, "lxml-xml")
    
    pdf_link_tag = oapi_soup.find('link')
    if(pdf_link_tag is None):
        print('No PDF found for that DOI')
        return
    
    pdf_url = pdf_link_tag['href']
    if pdf_url.startswith('ftp:'):
        pdf_url = pdf_url.replace('ftp:','https:') 
    file_path = Path(base_file_path + '/' + doi + '.pdf')
    parent_dir = file_path.parent
    if os.path.exists(parent_dir) is False:
        os.makedirs(parent_dir)
    download_file(pdf_url, file_path)   

# %% ../../nbs/35_localdb.ipynb 8
@dataclass
class QuerySpec:
    name: str
    id_col: str
    query_col: str
    name_col: str
    col_map: dict[str, str] = field(default_factory=dict)
    sections: list[str] = field(default_factory=list)

    def process_cdf(self, cdf: pd.DataFrame):
        cdf = cdf.rename(columns={self.id_col:'ID', self.query_col:'QUERY'})
        cdf = cdf.rename(columns=self.col_map)
        cdf = cdf.fillna('').rename(
            columns={c:re.sub('[\s\(\)]','_', c.upper()) for c in cdf.columns}
            )
        cdf.QUERY = [re.sub('^http[s]*://', '', r.QUERY) if r.QUERY[:4]=='http' else r.QUERY 
                     for i,r in cdf.iterrows()] 
        cdf.QUERY = [re.sub('/$', '', r.QUERY.strip())  
                        for i,r in cdf.iterrows()]
        return cdf

class LocalLiteratureDb:
  
  """This class runs a set of queries on external literature databases to build a local database of linked corpora and papers.

  Functionality includes:

    * Define a spreadsheet with a column of queries expressed in boolean logic
    * Optional: Define a secondary spreadsheet with a column of subqueries expressed in boolean logic
    * Iterate over sources (currently only European PMC, but possibly others) to execute all combinations of queries and subqueries
    * Builds a local SQLite database with tables for collections, expressions, items, and fragments. 
    * Provides an API for querying the database and returning results as sqlAlchemy objects.
  """

  def __init__(self, loc, name):
    self.name = name
    
    if loc[-1] != '/':
      loc = loc + '/' 
    self.loc = loc
    if os.path.exists(loc) is False:
      os.mkdir(loc)

    db_path = Path(loc+name+'/sciknow.db')
    db_dir = db_path.parent
    if db_dir.exists() is False:
      os.makedirs(db_dir)

    if db_path.exists() is False:
      schema_sql = files(linkml).joinpath('schema.sql').read_text()
      connection = sqlite3.connect(db_path)
      cursor = connection.cursor()
      cursor.executescript(schema_sql) 
    
    self.engine = create_engine('sqlite:///'+loc+name+'/sciknow.db')
    self.session = None # instantiate session when needed

    log_path = '%s%s_log.txt'%(loc, name)
    if os.path.exists(log_path) is False:
      Path(log_path).touch()

  def add_sections_as_fragments_from_nxmldoc(self, item, d):
    """Builds a set of fragments from an NxmlDoc object"""

    # ['PMID', 'PARAGRAPH_ID', 'TAG', 'TAG_TREE', 'OFFSET', 'LENGTH', 'FIG_REF', 'PLAIN_TEXT'
    fragments = []
    try: 
      df = d.build_simple_document_dataframe()
    except Exception as ex:
      return
    
    # Can search for a substring in top section headers
    # df3 = df[df.TOP_SECTION.str.contains('method', case=False)]

    df3 = df[df.TOP_SECTION!='']
    df4 = df3.groupby('SECTION_TREE').agg({'OFFSET': 'min', 'LENGTH': 'sum', 'PLAIN_TEXT':lambda x: '\n'.join(x)}).sort_values('OFFSET')
    df4 = df4.reset_index(drop=False)
    
    if df4 is None:
      return
    
    for i, tup in df4.iterrows():      
      fragment = ScientificKnowledgeFragment(id=item.id[:10]+'.'+str(i), 
                                             type='section',
                                             offset=tup.OFFSET,
                                             length=tup.LENGTH,
                                             name=tup.SECTION_TREE,
                                             content=tup.PLAIN_TEXT)
      self.session.add(fragment)
      self.session.flush()
      item.has_part.append(fragment)
      fragment.part_of = item.id
      fragments.append(fragment)
      self.session.flush()     

  def add_fragments_from_nxmldoc(self, item, d):
    """Builds a set of fragments from an NxmlDoc object"""

    # ['PMID', 'PARAGRAPH_ID', 'TAG', 'TAG_TREE', 'OFFSET', 'LENGTH', 'FIG_REF', 'PLAIN_TEXT'
    fragments = []
    df = d.build_enahanced_document_dataframe()
    if df is None:
      return
    for i, tup in d.build_enahanced_document_dataframe().iterrows():      
      fragment = ScientificKnowledgeFragment(id=item.id[:10]+'.'+str(tup.PARAGRAPH_ID), 
                                             type=tup.TAG,
                                             offset=tup.OFFSET,
                                             length=tup.LENGTH,
                                             content=tup.PLAIN_TEXT)
      self.session.add(fragment)
      self.session.flush()
      item.has_part.append(fragment)
      fragment.part_of = item.id
      fragments.append(fragment)
      self.session.flush()     

  def add_full_text_for_expression(self, e,  
                                   get_nxml=True, 
                                   get_pdf=False, 
                                   get_html=False):
    doi = read_information_content_entity_iri(e, 'doi')
    if doi is None:
      return  

    # Copy file to local directory
    base_file_path = '%s%s/nxml/'%(self.loc, self.name)
    if get_nxml:
      nxml_file_path = base_file_path+doi+'.nxml'
      if(os.path.exists(nxml_file_path) is False):
        try:
          get_nxml_from_pubmed_doi(doi, base_file_path)
        except Exception as ex:
          return
      if os.path.exists(nxml_file_path):
        with open(nxml_file_path, 'r') as f:
          xml = f.read()
          try:
            d = NxmlDoc(doi, xml)
          except Exception as ex:
            return
          doc_text = d.text 
          if 'body' in [so.element.tag for so in d.standoffs]:
            ski_type = 'FullTextPaper'
          else:
            ski_type = 'CitationRecord'     
          ski = ScientificKnowledgeItem(id=str(uuid.uuid4().hex), 
                                              content=doc_text,
                                              xref=['file:'+nxml_file_path],
                                              type=ski_type,)
          e.has_representation.append(ski)
          self.session.add(ski)
          self.session.flush()
          self.add_sections_as_fragments_from_nxmldoc(ski, d)

    if get_pdf:
      #get_pdf_from_pubmed_doi(doi, base_file_path)
      placeholder = 1

    if get_html:
      placeholder = 1   

  def add_full_text_for_collection(self, collection_id, 
                                   get_nxml=True, get_pdf=True, get_html=True):
    for e in self.list_expressions(collection_id=collection_id):
      doi = read_information_content_entity_iri(e, 'doi')
      if doi is None:
        continue  
      self.add_full_text_for_expression(e, get_nxml, get_pdf, get_html)      

  def add_corpus_from_epmc(self, qt, qt2, sections=['paper_title', 'ABSTRACT'], sections2=['paper_title', 'ABSTRACT']):
    """Adds corpora based on coupled QueryTranslator objects."""
    
    if self.session is None:
      session_class = sessionmaker(bind=self.engine)
      self.session = session_class()

    if self.session.query(exists().where(InformationResource.name=='EPMC')).scalar():
      info_resource = self.session.query(InformationResource) \
          .filter(InformationResource.name=='EPMC').first()
    else:
      info_resource = InformationResource(id='skem:EPMC', 
                                          iri=['skem:EPMC'], 
                                          name='European PubMed Central', 
                                          type='skem:InformationResource',
                                          xref=['https://europepmc.org/'])

    (corpus_ids, epmc_queries) = qt.generate_queries(QueryType.epmc, sections=sections)
    if qt2:
      (subset_ids, epmc_subset_queries) = qt2.generate_queries(QueryType.epmc, sections=sections2)
    else: 
      (subset_ids, epmc_subset_queries) = ([0],[''])
    for (i, q) in zip(corpus_ids, epmc_queries):
      for (j, sq) in zip(subset_ids, epmc_subset_queries):
        query = q
        corpus_id = str(i)
        corpus_name = qt.df.iloc[i][qt.name_col]
        if query is None or query=='nan' or len(query)==0: 
          continue
        if len(sq) > 0:
          query = '(%s) AND (%s)'%(q, sq)
          corpus_id = str(i)+'.'+str(j)
          corpus_name2 = qt2.df.iloc[j][qt2.name_col]
          corpus_name = corpus_name + '/'+ corpus_name2
        
        # does this collection already exist?  
        if self.session.query(exists().where(ScientificKnowledgeCollection.id==corpus_id)).scalar():
          cp = self.session.query(ScientificKnowledgeCollection) \
              .join(ScientificKnowledgeCollection.has_members, isouter=True) \
              .filter(ScientificKnowledgeCollection.id==corpus_id).first()
          if cp is not None:
            for p in cp.has_members:
              cp.has_members.remove(p)
            self.session.flush()
            self.session.delete(cp)
            self.session.commit()

        corpus = ScientificKnowledgeCollection(id=corpus_id,
                                                           type='skem:ScientificKnowledgeCollection',
                                                           provenance=[query], 
                                                           name=corpus_name,
                                                           has_members=[])
        self.session.add(corpus)
        self.session.commit()

        epmcq = EuroPMCQuery()
        numFound, pubs = epmcq.run_empc_query(query)
        for p in tqdm(pubs):
          p_id = str(p.id)
          p_check = self.session.query(ScientificKnowledgeExpression) \
              .filter(ScientificKnowledgeCollection.id==p_id).first()
          if p_check is not None:
            p = p_check
          corpus.has_members.append(p)
          for item in p.has_representation:
            for f in item.has_part:          
              f.part_of = item.id
              self.session.add(f)
              self.session.flush()
            item.represented_by = p.id
            self.session.add(item)
            self.session.flush()
          self.session.add(p)
          self.session.flush()
        self.session.commit()

  def check_query_terms(self, qt, qt2=None, pubmed_api_key=''):
    pmq = ESearchQuery(api_key=pubmed_api_key)
    terms = set()
    for t in qt.terms2id.keys():
        terms.add(t)
    if qt2 is not None:
        for t2 in qt2.terms2id.keys():
            terms.add(t2)
    check_table = {} 
    for t in tqdm(terms):
        (is_ok, t2, c) = pmq._check_query_phrase(t)
        check_table[t] = (is_ok, c)
    return check_table
  
  def list_collections(self, search_term=None):
    if self.session is None:
      session_class = sessionmaker(bind=self.engine)
      self.session = session_class()
    if search_term:
      q = (self.session.query(ScientificKnowledgeCollection) 
          .filter(ScientificKnowledgeCollection.name == search_term))
    else:
      q = self.session.query(ScientificKnowledgeCollection)
    for c in q.all():
      yield(c)

  def list_expressions(self, collection_id=None, search_term=None): 
    if self.session is None:
      session_class = sessionmaker(bind=self.engine)
      self.session = session_class()
    if collection_id:
      if search_term:
        search = "%{}%".format(search_term)
        q = (self.session.query(ScientificKnowledgeCollectionHasMembers,
                              ScientificKnowledgeExpression,
                              ScientificKnowledgeExpressionHasRepresentation,
                              ScientificKnowledgeItem) 
            .filter(ScientificKnowledgeCollectionHasMembers.ScientificKnowledgeCollection_id==collection_id)
            .filter(ScientificKnowledgeCollectionHasMembers.has_members_id == ScientificKnowledgeExpression.id)
            .filter(ScientificKnowledgeExpression.id == ScientificKnowledgeExpressionHasRepresentation.ScientificKnowledgeExpression_id)
            .filter(ScientificKnowledgeExpressionHasRepresentation.has_representation_id == ScientificKnowledgeItem.id)
            .filter(ScientificKnowledgeItem.content.like(search))
          )
      else:
         q = (self.session.query(ScientificKnowledgeCollection, 
                              ScientificKnowledgeCollectionHasMembers,
                              ScientificKnowledgeExpression ) 
            .filter(ScientificKnowledgeCollection.id == ScientificKnowledgeCollectionHasMembers.ScientificKnowledgeCollection_id)
            .filter(ScientificKnowledgeCollectionHasMembers.has_members_id == ScientificKnowledgeExpression.id)
            .filter(ScientificKnowledgeCollection.id == collection_id)
          )
    else:
      if search_term:
        search = "%{}%".format(search_term)
        q = (self.session.query(ScientificKnowledgeExpression,
                              ScientificKnowledgeExpressionHasRepresentation,
                              ScientificKnowledgeItem) 
            .filter(ScientificKnowledgeCollectionHasMembers.has_members_id == ScientificKnowledgeExpression.id)
            .filter(ScientificKnowledgeExpression.id == ScientificKnowledgeExpressionHasRepresentation.ScientificKnowledgeExpression_id)
            .filter(ScientificKnowledgeExpressionHasRepresentation.has_representation_id == ScientificKnowledgeItem.id)
            .filter(ScientificKnowledgeItem.content.like(search))
          )
      else:
        q = self.session.query(ScientificKnowledgeExpression)
      
    for c in q.all():
      yield(c)

  def list_notes_for_fragments_in_paper(self, run_name, paper_id, item_type='FullTextPaper'):
    '''returns notes of a specific type associated with fragments from a given paper .'''
    q1 = self.session.query(ScientificKnowledgeItem) \
            .filter(ScientificKnowledgeExpression.id == ScientificKnowledgeExpressionHasRepresentation.ScientificKnowledgeExpression_id) \
            .filter(ScientificKnowledgeExpressionHasRepresentation.has_representation_id == ScientificKnowledgeItem.id) \
            .filter(ScientificKnowledgeItem.type == item_type) \
            .filter(ScientificKnowledgeExpression.id.like('%'+str(paper_id)+'%')) 
    i = q1.first()
    if i is None:
      return []
    for f in i.has_part:
      for n in f.has_notes:
        if n.name == run_name:
          yield(n)
         
  def list_fragments_for_paper(self, paper_id, item_type='FullTextPaper'):
    '''Loads fragments from a given paper sections of a specified paper from the local database.'''
    q1 = self.session.query(ScientificKnowledgeItem) \
            .filter(ScientificKnowledgeExpression.id == ScientificKnowledgeExpressionHasRepresentation.ScientificKnowledgeExpression_id) \
            .filter(ScientificKnowledgeExpressionHasRepresentation.has_representation_id == ScientificKnowledgeItem.id) \
            .filter(ScientificKnowledgeItem.type == item_type) \
            .filter(ScientificKnowledgeExpression.id.like('%'+str(paper_id)+'%')) 
    i = q1.first()
    if i is None:
        raise Exception('No items of format: %s found for expression: %s'%(item_type, str(paper_id)))
    fragments = []
    for f in i.has_part:
      fragments.append(f)
    return sorted(fragments, key=lambda f: f.offset)
  
  def list_fragments(self, expression_id=None, search_term=None):
    if self.session is None:
      session_class = sessionmaker(bind=self.engine)
      self.session = session_class()
    if expression_id:
      if search_term:
        search = "%{}%".format(search_term)
        q = (self.session.query(ScientificKnowledgeExpressionHasRepresentation,
                              ScientificKnowledgeItem,
                              ScientificKnowledgeItemHasPart,
                              ScientificKnowledgeFragment) 
            .filter(ScientificKnowledgeExpressionHasRepresentation.ScientificKnowledgeExpression_id == expression_id)
            .filter(ScientificKnowledgeExpressionHasRepresentation.has_representation_id == ScientificKnowledgeItem.id)
            .filter(ScientificKnowledgeItem.id == ScientificKnowledgeItemHasPart.ScientificKnowledgeItem_id)
            .filter(ScientificKnowledgeItemHasPart.has_part_id == ScientificKnowledgeFragment.id)
            .filter(ScientificKnowledgeFragment.content.ilike('%'+search+'%'))
          )
      else:
        q = (self.session.query(ScientificKnowledgeExpressionHasRepresentation,
                              ScientificKnowledgeItem,
                              ScientificKnowledgeItemHasPart,
                              ScientificKnowledgeFragment) 
            .filter(ScientificKnowledgeExpressionHasRepresentation.ScientificKnowledgeExpression_id == expression_id)
            .filter(ScientificKnowledgeExpressionHasRepresentation.has_representation_id == ScientificKnowledgeItem.id)
            .filter(ScientificKnowledgeItem.id == ScientificKnowledgeItemHasPart.ScientificKnowledgeItem_id)
            .filter(ScientificKnowledgeItemHasPart.has_part_id == ScientificKnowledgeFragment.id)
          )
    else:
      if search_term:
        search = "%{}%".format(search_term)
        q = (self.session.query(ScientificKnowledgeExpressionHasRepresentation,
                              ScientificKnowledgeItem,
                              ScientificKnowledgeItemHasPart,
                              ScientificKnowledgeFragment) 
            .filter(ScientificKnowledgeExpressionHasRepresentation.has_representation_id == ScientificKnowledgeItem.id)
            .filter(ScientificKnowledgeItem.id == ScientificKnowledgeItemHasPart.ScientificKnowledgeItem_id)
            .filter(ScientificKnowledgeItemHasPart.has_part_id == ScientificKnowledgeFragment.id)
            .filter(ScientificKnowledgeFragment.content.ilike('%'+search+'%'))
          )
      else:
        q = self.session.query(ScientificKnowledgeFragment)
    for c in q.all():
      yield(c)

# %% ../../nbs/35_localdb.ipynb 9
#| export


