# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/12_jats_text_extractor.ipynb.

# %% auto 0
__all__ = ['TexOptions', 'U2aOptions', 'NxmlDoc']

# %% ../../nbs/12_jats_text_extractor.ipynb 2
from collections import namedtuple
from lxml import etree
from lxml.etree import ElementTree
from nxml2txt import rewritetex
from nxml2txt import rewritemmla
from nxml2txt import respace
from nxml2txt import rewriteu2a
from nxml2txt import standoff
from io import StringIO
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup,Tag,Comment,NavigableString
from urllib.request import urlopen
from requests.utils import requote_uri

import dataclasses
from enum import auto, Enum
from typing import List, Tuple, Any, Dict

import csv
import html
import string
import pandas as pd
import re
import requests


# %% ../../nbs/12_jats_text_extractor.ipynb 3
TexOptions = namedtuple('TexOptions', 'verbose')
U2aOptions = namedtuple('U2aOptions', 'hex keep_missing stdout directory overwrite')

@dataclasses.dataclass
class NxmlDoc:
    """A class that provides structure for full text papers specified under the JATS 'nxml' format."""

    # The XML content of the file
    xml: str

    # The identifier of the paper
    ft_id: str

    # Plain text of the paper's contents
    text: str

    # Standoff annotations superimposed over the  prompts
    standoffs: str
      
    def __init__(self, ft_id, xml):
        self.ft_id = ft_id

        # HTML entities kill the XML parse
        # but any '<' characters must be replaced with &lt; in XML (and '& with &amp;)
        xml = xml.replace('<', '__less_than__')
        xml = html.unescape(xml)
        xml = xml.replace('&', '&amp;')
        xml = xml.replace('<', '&lt;')
        xml = xml.replace('__less_than__', '<')
        xml = xml.encode('utf-8')
        self.xml = xml
        
        tree = ElementTree( etree.fromstring(xml) )
        tex_options = TexOptions(verbose=True)
        rewritetex.process_tree(tree, options=tex_options)
        
        # process MathML annotations
        rewritemmla.process_tree(tree)
        
        # normalize whitespace
        #respace.process_tree(tree)
        
        # map unicodoffs = nxml2txt(nxmlfne to ASCII)
        u2a_options = U2aOptions(keep_missing=True, hex=False, stdout=False, directory=None, overwrite=False)
        rewriteu2a.process_tree(tree, options=u2a_options)
        
        # convert to text and standoffs
        text, standoffs = standoff.convert_tree(tree)   
        self.text = text
        self.standoffs = standoffs

        self.to_exclude = ['table-wrap-foot']
        self.text_tag_types = ['front/article-title', 'front/abstract', 'body/p', 'body/title', 'body/label']
        self.tag_types = {'text':['article-title', 'abstract', 'p', 'title', 'label', 'caption'],
                'structure':['front', 'body', 'back', 'ref-list', 'sec', 'fig', 'supplementary-material'],
                'xref': ['xref', 'ref', 'label', 'name', 'surname', 'year', 'pub-id', 'fpage']}

    def get_figure_reference(self, t):
        pos = t.start
        hits = []
        for s in sorted(self.standoffs, key=lambda x: x.start):
          if pos>=s.start and pos<s.end and s!=t: 
            hits.append(s)
        for t in hits:
          if t.element.tag == 'fig':      
            return t.element.get('id','')
        return ''

    def get_top_level_sec_tag(self, t):
        pos = t.start
        hits = []
        for s in sorted(self.standoffs, key=lambda x: x.start):
          if pos>=s.start and pos<s.end and s!=t: 
            hits.append(s)
        for t in hits:
          if t.element.tag == 'sec':      
            if t.element.get('sec-type', None):
              return t.element.get('sec-type')
            elif t.element.find('title') is not None:
              return t.element.find('title').text
        return ''

    def generate_tag_tree(self, t):
        pos = t.start
        hits = []
        for s in sorted(self.standoffs, key=lambda x: x.start):
          if pos>=s.start and pos<s.end and s!=t: 
            hits.append(s)
        tag_tree = '.'.join(['%s[%s...]'%(t.element.tag,self.text[t.start:t.start+8]) if t.element.tag=='sec' else t.element.tag for t in hits])
        tag_tree = tag_tree+'.'+t.element.tag
        return tag_tree
    
    def build_simple_document_dataframe(self):

        text_tuples = []

        try:

            # two stage process - build a lookup list of all relevant tags 
            # - then use the tags start/end properties to identify text portions of the paper and render those.

            this_doc_standoffs = {t:[] for tt in self.tag_types.keys() for t in self.tag_types[tt]}
            
            all_xrefs = []
            for s in self.standoffs:
                if this_doc_standoffs.get(s.element.tag) is not None:
                    this_doc_standoffs.get(s.element.tag).append(s)
                if s.element.tag == 'xref':
                    all_xrefs.append(s)
            #
            # skip the whole file if there's no body tag.
            #
            if len(this_doc_standoffs.get('body')) == 0:
                return None
            
            text_so_list = []
            for ttt in self.text_tag_types:
                part,tag = ttt.split('/')
                part_so = this_doc_standoffs.get(part)[0]
                for so in this_doc_standoffs.get(tag):
                    if so.start < part_so.start or so.end > part_so.end:
                        continue
                    text_so_list.append(so)
                    #print((row.PMID, local_id, so.element.tag, query_document_standoffs(so, text, standoffs), so.start, (so.end-so.start), text[so.start:so.end]))
              
            # Manipulate standoff annotations so that titles and labels fall naturally in the text 
            # and paragraph tags that hold other paragraphs (as is the case with pmid:26791617) don't trigger repeating text.
            # Make sure the SOs only tile the document and do not overlap.
            text_so_list = sorted(text_so_list, key=lambda x: x.start)
            last_so = None
            for so in text_so_list:
                if last_so:
                    if last_so.end > so.start:
                        last_so.end = so.start-1
                last_so = so
              
            sent_id = 0
            for local_id, so in enumerate(text_so_list):
                #tag_tree = generate_tag_tree(so, text, standoffs)
                top_sec_title = self.get_top_level_sec_tag(so) 
                figure_reference = self.get_figure_reference(so) 
                so_text = self.text[so.start:so.end]
                                
                tuple = (self.ft_id, local_id, so.element.tag, top_sec_title, so.start, (so.end-so.start), figure_reference, so_text)
                text_tuples.append(tuple)
              
        except etree.XMLSyntaxError as xmlErr:
            print("XML Syntax Error: {0}".format(xmlErr))
        except UnicodeDecodeError as unicodeErr:
            print("Unicode parsing Error: {0}".format(unicodeErr))
        #except TypeError as typeErr:
        #  print("Type Error: {0}".format(typeErr))  
        #    print("ValueError: {0}".format(valErr))
        #    return None
        
        text_df = pd.DataFrame(text_tuples, columns=['PMID', 'PARAGRAPH_ID', 'TAG', 'TAG_TREE', 'OFFSET', 'LENGTH', 'FIG_REF', 'PLAIN_TEXT'])
        return text_df


    def build_enahanced_document_dataframe(self):

        text_tuples = []

        try:

            # two stage process - build a lookup list of all relevant tags 
            # - then use the tags start/end properties to identify text portions of the paper and render those.

            this_doc_standoffs = {t:[] for tt in self.tag_types.keys() for t in self.tag_types[tt]}
            
            all_xrefs = []
            for s in self.standoffs:
                if this_doc_standoffs.get(s.element.tag) is not None:
                    this_doc_standoffs.get(s.element.tag).append(s)
                if s.element.tag == 'xref':
                    all_xrefs.append(s)
            #
            # skip the whole file if there's no body tag.
            #
            if len(this_doc_standoffs.get('body')) == 0:
                return None
            
            ref_dict = self.extract_ref_dict_from_nxml()

            text_so_list = []
            for ttt in self.text_tag_types:
                part,tag = ttt.split('/')
                part_so = this_doc_standoffs.get(part)[0]
                for so in this_doc_standoffs.get(tag):
                    if so.start < part_so.start or so.end > part_so.end:
                        continue
                    text_so_list.append(so)
                    #print((row.PMID, local_id, so.element.tag, query_document_standoffs(so, text, standoffs), so.start, (so.end-so.start), text[so.start:so.end]))
              
            # Manipulate standoff annotations so that titles and labels fall naturally in the text 
            # and paragraph tags that hold other paragraphs (as is the case with pmid:26791617) don't trigger repeating text.
            # Make sure the SOs only tile the document and do not overlap.
            text_so_list = sorted(text_so_list, key=lambda x: x.start)
            last_so = None
            for so in text_so_list:
                if last_so:
                    if last_so.end > so.start:
                        last_so.end = so.start-1
                last_so = so
              
            sent_id = 0
            for local_id, so in enumerate(text_so_list):
                #tag_tree = generate_tag_tree(so, text, standoffs)
                top_sec_title = self.get_top_level_sec_tag(so) 
                figure_reference = self.get_figure_reference(so) 
                
                # ANY EXCLUSION CRITERIA FOR TAGS PUT IT HERE
                
                # SEARCH FOR XREFS IN THIS TEXT BLOCK - AND SUB THEM INTO THE TEXT.
                so_text = ''
                prev_end = so.start
                ref_xrefs = [x for x in all_xrefs if x.start>=so.start and x.end<=so.end and x.element.attrib['ref-type']=='bibr']
                #print(ref_xrefs)
                
                if len(ref_xrefs) > 0:
                    refbib_xrefs = [x for x in all_xrefs if x.start>=so.start and x.end<=so.end and 
                                (x.element.attrib['ref-type']=='bibr' or x.element.attrib['ref-type']=='fig')] 
                    for x in refbib_xrefs:
                        if x.element.attrib['ref-type']=='bibr':
                            ref_id = x.element.attrib['rid']
                            ref = ref_dict.get(ref_id, None)
                            if ref and ref.get('pmid'):
                                ref_text= '<<REF:%s>>'%(ref.get('pmid'))
                            elif ref:
                                ref_text= '<<REF:%s-%s-%s-%s>>'%(ref.get('first_author','???'),ref.get('year','?'),ref.get('vol','?'),ref.get('page','?'))
                            else:
                                ref_text = '<<REF>>'
                            so_text += self.text[prev_end:x.start] + ref_text
                        else: 
                            fig_id = x.element.attrib['rid']
                            fig_text = '%s <<FIG:%s>>'%(self.text[x.start:x.end],fig_id)
                            so_text += self.text[prev_end:x.start] + fig_text
                        #print(pmid, ref_id, ref_text)
                        prev_end = x.end
                    
                    #if len(so_text)>0:
                    #  print(so_text)
                    so_text += self.text[prev_end:so.end]  
                    so_text = html.unescape(so_text)
                #__________________________________________________________________
                else: # TRY TO USE REGEXES TO SUBSTITUTE REFERENCES IN PASSAGE TEXT
                    fig_xrefs = [x for x in all_xrefs if x.start>=so.start and x.end<=so.end and x.element.attrib['ref-type']=='fig']
                    so_text = ''
                    prev_end = so.start
                    for x in fig_xrefs:
                        fig_id = x.element.attrib['rid']
                        fig_text = '%s <<FIG:%s>>'%(self.text[x.start:x.end],fig_id)
                        so_text += self.text[prev_end:x.start] + fig_text
                        prev_end = x.end
                    so_text += self.text[prev_end:so.end]  
                    so_text = html.unescape(so_text)

                    #print(so_text)
                    for key in ref_dict:
                        ref = ref_dict[key]
                        if ref.get('pmid'):  
                            ref_text= '<<REF:%s>>'%(ref.get('pmid'))
                        else:
                            ref_text= '<<REF:%s-%s-%s-%s>>'%(ref.get('first_author','???'),ref.get('year','?'),ref.get('vol','?'),ref.get('page','?'))
                        if ref.get('year') and ref.get('second_author'):
                            regex = '%s( and %s,|,|\\s+et al\\.\\,|\\s+et al){0,1}\\s+%s'%(ref.get('first_author',''),ref.get('second_author',''),ref.get('year',''))
                        elif ref.get('year') and len(ref.get('first_author',''))>0:
                            regex = '%s(,|\\s+et al\\.\\,|\\s+et al){0,1}\\s+%s'%(ref.get('first_author',''),ref.get('year',''))
                        else:
                            regex = '%s( and [A-Za-z]+|,|\\s+et al\\.\\,|\\s+et al){0,1}\\s+(19|20)[0-9][0-9]'%(ref.get('first_author',''))
                        pattern = re.compile(regex)
                        if pattern.search(so_text):
                            so_text = pattern.sub(ref_text, so_text)
                        #print( pattern.sub(ref_text,so_text))
                
                tuple = (self.ft_id, local_id, so.element.tag, top_sec_title, so.start, (so.end-so.start), figure_reference, so_text)
                text_tuples.append(tuple)
              
        except etree.XMLSyntaxError as xmlErr:
            print("XML Syntax Error: {0}".format(xmlErr))
        except UnicodeDecodeError as unicodeErr:
            print("Unicode parsing Error: {0}".format(unicodeErr))
        #except TypeError as typeErr:
        #  print("Type Error: {0}".format(typeErr))  
        #    print("ValueError: {0}".format(valErr))
        #    return None
        
        text_df = pd.DataFrame(text_tuples, columns=['PMID', 'PARAGRAPH_ID', 'TAG', 'TAG_TREE', 'OFFSET', 'LENGTH', 'FIG_REF', 'PLAIN_TEXT'])
        return text_df
    
    def extract_ref_dict_from_nxml(self):

        if self.xml is None:
            return

        soup = BeautifulSoup(self.xml, "lxml")

        references = soup.find_all('ref')
        all_ref_dict = {}
        for r in references:
            ref_dict = {}
            ref_dict['ref'] = r.attrs.get('id')

            ref_dict['author'] = ''
            for t in r.descendants:
                if type(t) is Tag and t.name == 'surname' and ref_dict.get('first_author', None) is None:
                    ref_dict['first_author'] = re.sub("'","''",t.text)
                if type(t) is Tag and t.name == 'surname' and ref_dict.get('first_author', None) is not None:
                    ref_dict['second_author'] = re.sub("'","''",t.text)
                if type(t) is Tag and t.name == 'name' and len(ref_dict.get('author')) > 0:
                    ref_dict['author'] += ', '
                if type(t) is Tag and t.name == 'surname':
                    ref_dict['author'] += re.sub("'","''",t.text)
                if type(t) is Tag and t.name == 'given-names':
                    ref_dict['author'] += ' ' + re.sub("'","''",t.text)
                elif type(t) is Tag and t.name == 'article-title':
                    ref_dict['title'] = re.sub("'","''",t.text)
                elif type(t) is Tag and t.name == 'source':
                    ref_dict['journal'] = t.text
                elif type(t) is Tag and t.name == 'year':
                    m = re.match('(\\d\\d\\d\\d)', t.text)
                    if m:
                        ref_dict['year'] = m.group(1)
                elif type(t) is Tag and t.name == 'volume':
                    ref_dict['vol'] = t.text
                elif type(t) is Tag and t.name == 'fpage':
                    ref_dict['page'] = t.text
                    
            all_ref_dict[ref_dict.get('ref')] = ref_dict
        
        # Search pubmed for the PMIDs
        # Need to add this back to the dict but cannot link data from pubmed ids to the original references
        '''
        clauses = []
        for r in all_ref_dict: 
            ref_dict = all_ref_dict[r]
            if ref_dict.get('first_author', None) is not None and \
                    ref_dict.get('year', None) is not None and \
                    ref_dict.get('vol', None) is not None and \
                    ref_dict.get('page', None) is not None:
                c = "(%s[au]+AND+%s[dp]+AND+%s[vi]+AND+%s[pg]')"%(
                        ref_dict.get('first_author'),
                        ref_dict.get('year'), 
                        ref_dict.get('vol'), 
                        ref_dict.get('page')
                    )     
                clauses.append(c)
        
        if len(clauses)==0:
            return all_ref_dict

        stem = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?api_key='+pubmed_api_key
        pmids = []
        for i in range(0, len(clauses), 50):
            query = '+OR+'.join(clauses[i:i+50])
            r = requests.get(stem+'&db=pubmed&term='+query)
            soup2 = BeautifulSoup(r.text, "lxml")
            for id in soup2.find_all('id'):
                pmids.append(id.text)

        # Search pubmed for the PMIDs
        # query pubmed for the pmid
        
        #print('\n'+lookup_sql+'\n\n')
        lookup_df = execute_query(cs, lookup_sql, ['PMID', 'FIRST_AUTHOR', 'YEAR', 'VOLUME', 'PAGE'])
        lookup = {('%s-%s-%s-%s'%(row.FIRST_AUTHOR, row.YEAR, row.VOLUME, row.PAGE)).lower():row.PMID for row in lookup_df.itertuples()}      
        
        #print('doc: ', end = '')
        for r in all_ref_dict: 
            ref_dict = all_ref_dict[r]
            if ref_dict.get('first_author', None) is not None and ref_dict.get('year', None) is not None and ref_dict.get('vol', None) is not None and ref_dict.get('page', None) is not None :
            au = ref_dict['first_author']
            dp = ref_dict['year']
            vo = ref_dict['vol']
            pg = ref_dict['page']
            pmid = lookup.get(('%s-%s-%s-%s'%(au, dp, vo, pg)).lower(), None)
            if pmid: 
                ref_dict['pmid'] = pmid
                #print('.', end = '')
        #print()
        '''
        
        return all_ref_dict
    
