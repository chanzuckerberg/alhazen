# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/20_metadata_extraction_tool.ipynb.

# %% auto 0
__all__ = ['MetadataExtractionTool']

# %% ../../nbs/20_metadata_extraction_tool.ipynb 3
import local_resources.linkml as linkml

from ..core import OllamaRunner, PromptTemplateRegistry, get_langchain_llm, get_cached_gguf, get_langchain_embeddings, GGUF_LOOKUP_URL, MODEL_TYPE
from ..utils.airtableUtils import AirtableUtils
from ..utils.searchEngineUtils import ESearchQuery, EuroPMCQuery
from ..utils.langchain_utils import suppress_stdout_stderr
from ..utils.output_parsers import JsonEnclosedByTextOutputParser

from ..utils.queryTranslator import QueryTranslator, QueryType
from ..utils.jats_text_extractor import NxmlDoc
from ..utils.local_literature_db import *

from alhazen.schema_sqla import ScientificKnowledgeCollection, ScientificKnowledgeExpression, \
    ScientificKnowledgeFragment, Note, ScientificKnowledgeCollection, \
    ScientificKnowledgeExpression, ScientificKnowledgeCollectionHasMembers, \
    ScientificKnowledgeItem, ScientificKnowledgeExpressionHasRepresentation, \
    ScientificKnowledgeFragment, ScientificKnowledgeItemHasPart, \
    InformationResource

from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.schema.runnable import RunnableLambda
from langchain.schema import OutputParserException
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.chains.combine_documents import collapse_docs, split_list_of_docs
from langchain.llms import LlamaCpp 
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

from importlib_resources import files
import local_resources.prompt_elements as prompt_elements

from bs4 import BeautifulSoup,Tag,Comment,NavigableString
from datetime import datetime
from importlib_resources import files
import json
import os
import pandas as pd
from pathlib import Path
import re
import requests
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from time import time,sleep
from tqdm import tqdm
from urllib.request import urlopen
from urllib.parse import quote_plus, quote, unquote
from urllib.error import URLError, HTTPError
import uuid
import yaml

# %% ../../nbs/20_metadata_extraction_tool.ipynb 5
class MetadataExtractionTool:
    '''Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'''

    lldb = None
    step_identification_prompt_template = None
    metadata_extraction_prompt_template = None
    methodology = None
    method_goal = None
    all_protocol_steps = None
    all_protocol_step_codes = None
    metadata_specs: []
    run_name = None
    
    def __init__(self, lldb, prompt_element_spec_name, llm_model='llama2:70b'):
        self.lldb = lldb
        if self.lldb.session is None:
            session_class = sessionmaker(bind=self.lldb.engine)
            self.lldb.session = session_class()

        pts = PromptTemplateRegistry()
        pts.load_prompts_from_yaml('metadata_extraction.yaml')
        self.step_identification_prompt_template = pts.get_prompt_template('protocol step identification').generate_llama2_prompt_template()
        self.metadata_extraction_prompt_template = pts.get_prompt_template('metadata extraction').generate_llama2_prompt_template()
        self.run_name = 'metadata_extraction_' + re.sub(' ','_',prompt_element_spec_name)

        # loading the additional elements from the yaml file
        # Note that there is an implicit assumption that the additional elements are formatted correctly. 
        # This code will throw an exception if the yaml file is not formatted correctly.
        prompt_elements_yaml = files(prompt_elements).joinpath('metadata_extraction.yaml').read_text()
        prompt_elements_dict = yaml.safe_load(prompt_elements_yaml).get(prompt_element_spec_name)
        self.method_goal = prompt_elements_dict['method goal']
        self.methodology = prompt_elements_dict['methodology']
        self.all_protocol_steps = prompt_elements_dict['all protocol steps']
        self.all_protocol_step_codes = prompt_elements_dict['all protocol step codes']
        self.metadata_specs = prompt_elements_dict['metadata specs']

        self.ollr = OllamaRunner(llm_model)
        self.llm  = self.ollr.llm

        self.protocol_step_id_lcel = self.step_identification_prompt_template | self.llm | JsonEnclosedByTextOutputParser()
        self.extract_lcel = self.metadata_extraction_prompt_template | self.llm | JsonEnclosedByTextOutputParser()

    def run(self, paper_id, section_name):
        '''Runs the metadata extraction pipeline over a specified paper.'''
        
        # Load the paper + fragments from the local database
        fragments = self.lldb.list_fragments_for_paper(paper_id)
    
        for f in fragments:
            if len(f.content) <= 50:
                continue
            
            if section_name not in f.name.lower():
                continue
            
            s1 = {'section_text':f.content,
                  'methodology': self.methodology,
                  'method_goal': self.method_goal,
                  'all_protocol_steps': self.all_protocol_steps,
                  'all_protocol_step_codes': self.all_protocol_step_codes
                 }
            protocol_step = None
            attempts = 0
            while protocol_step is None and attempts < 5:
                try: 
                    #with suppress_stdout_stderr():
                    out1 = self.protocol_step_id_lcel.invoke(s1, config={'callbacks': [ConsoleCallbackHandler()]})
                    if out1 is not None:
                        protocol_step = out1.get('protocol_step', None)
                    else: 
                        protocol_step = 'X'
                except OutputParserException as e:
                    attempts += 1
                    print(e) 
                    print('Retrying...')
                    
            #print('\t'+protocol_step)  
            for spec in self.metadata_specs:
                if protocol_step not in spec.get('step') :
                    continue
                s2 = {'section_text':f.content, 
                      'methodology': self.methodology,
                      'method_goal': self.method_goal,
                      'metadata_specification': spec.get('spec'), 
                      'metadata_name': spec.get('name') }
                
                try:
                    #with suppress_stdout_stderr():
                    out2 = self.extract_lcel.invoke(s2, config={'callbacks': [ConsoleCallbackHandler()]})
                except OutputParserException as e:
                    continue
                if out2 is not None:
                    # serialize out2 as json
                    note_content = json.dumps(out2)
                    
                    # add a fragment to the database                    
                    n = Note(
                        id=uuid.uuid4().hex[0:10],
                        type='NoteAboutFragment', 
                        name=self.run_name,
                        content=note_content, 
                        creation_date=datetime.now(), 
                        format='json')
                    n.is_about.append(f)
                    self.lldb.session.add(n)
                    self.lldb.session.flush()

        # commit the changes to the database
        self.lldb.session.commit()

    def tabulate_fragments(self, paper_id):
        q1 = self.lldb.session.query(ScientificKnowledgeItem) \
            .filter(ScientificKnowledgeExpression.id == ScientificKnowledgeExpressionHasRepresentation.ScientificKnowledgeExpression_id) \
            .filter(ScientificKnowledgeExpressionHasRepresentation.has_representation_id == ScientificKnowledgeItem.id) \
            .filter(ScientificKnowledgeItem.type == 'FullTextPaper') \
            .filter(ScientificKnowledgeExpression.id.like('%'+paper_id+'%')) 
        i = q1.first()
        l = []  
        for f in i.has_part:
            for n in f.has_notes:
                if n.name == self.run_name:
                    d = json.loads(n.content)
                    d['section'] = f.name
                    d['offset'] = f.offset
                    d['length'] = f.length
                    l.append(d)
        df = pd.DataFrame(l)
        df_pivot = df.pivot(index='metadata_name', columns=['offset', 'section'], values='metadata_value').fillna('')
        return df, df_pivot