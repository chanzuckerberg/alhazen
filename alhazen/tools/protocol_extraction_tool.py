# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/tools/23_protocol_extraction_tool.ipynb.

# %% auto 0
__all__ = ['skc', 'skc_hm', 'ske', 'ske_hr', 'ski', 'ski_hp', 'skf', 'n', 'skc_hn', 'ske_hn', 'ski_hn', 'skf_hn',
           'ProtocolExtractionToolSchema', 'BaseProtocolExtractionTool', 'ProcotolDiagramExtractionTool',
           'ProcotolEntitiesExtractionTool', 'ProcotolProcessesExtractionTool']

# %% ../../nbs/tools/23_protocol_extraction_tool.ipynb 3
from ..core import PromptTemplateRegistry
from .basic import AlhazenToolMixin
from ..utils.output_parsers import *
from ..utils.ceifns_db import *
from ..schema_sqla import *
from datetime import datetime
from importlib_resources import files
import jmespath
import json

from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field, root_validator
from langchain.schema import get_buffer_string, StrOutputParser, OutputParserException, format_document
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain.tools import BaseTool, StructuredTool
from langchain_core.output_parsers import JsonOutputParser
from langchain.vectorstores.pgvector import PGVector

import local_resources.prompt_elements as prompt_elements
import local_resources.linkml as linkml
from operator import itemgetter
import os
import pandas as pd
import re
import regex
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker, aliased
from time import time,sleep
from urllib.request import urlopen
from urllib.parse import quote_plus, quote, unquote
import uuid
import yaml

# %% ../../nbs/tools/23_protocol_extraction_tool.ipynb 4
skc = aliased(ScientificKnowledgeCollection)
skc_hm = aliased(ScientificKnowledgeCollectionHasMembers)
ske = aliased(ScientificKnowledgeExpression)
ske_hr = aliased(ScientificKnowledgeExpressionHasRepresentation)
ski = aliased(ScientificKnowledgeItem)
ski_hp = aliased(ScientificKnowledgeItemHasPart)
skf = aliased(ScientificKnowledgeFragment)
n = aliased(Note)
skc_hn = aliased(ScientificKnowledgeCollectionHasNotes)
ske_hn = aliased(ScientificKnowledgeExpressionHasNotes)
ski_hn = aliased(ScientificKnowledgeItemHasNotes)
skf_hn = aliased(ScientificKnowledgeFragmentHasNotes)

# %% ../../nbs/tools/23_protocol_extraction_tool.ipynb 5
class ProtocolExtractionToolSchema(BaseModel):
    paper_id: str = Field(description="the doi of the paper being analyzed, must start with the string 'doi:'")
    
class BaseProtocolExtractionTool(BaseTool, AlhazenToolMixin):
    '''Runs a specified protocol extraction pipeline over a research paper that has been loaded in the local literature database.'''
    name = 'protocol_workflow_extraction'
    description = 'Runs a specified protocol extraction pipeline over a research paper that has been loaded in the local literature database.'
    args_schema = ProtocolExtractionToolSchema
    return_direct:bool = True

    def _run(self, paper_id, extraction_type):
        '''Runs a specified protocol extraction pipeline over a research paper that has been loaded in the local literature database.'''
        raise NotImplementedError('This method must be implemented by a subclass.')

# %% ../../nbs/tools/23_protocol_extraction_tool.ipynb 6
class ProcotolDiagramExtractionTool(BaseProtocolExtractionTool):
    '''Extracts a mermaid diagram of the protocol from a paper.'''
    name = 'protocol_diagram_extraction'
    description = 'Extracts a mermaid diagram of the protocol from a paper.'

    def _run(self, paper_id):
        '''Extracts a mermaid diagram of the protocol from a paper.'''

        if self.db.session is None:
            session_class = sessionmaker(bind=self.db.engine)
            self.db.session = session_class()

        # Introspect the class name of the llm model for notes and logging
        llm_class_name = self.llm.__class__.__name__

        run_metadata = {
            'tool': self.__class__.__name__,
            'doi': paper_id,
            'llm_class': llm_class_name}

        # 0. Use the first available full text item type
        item_types = set()
        item_type = None
        for i in self.db.list_items_for_expression(paper_id):
            item_types.add(i.type)
        for i_type in item_types:
            if i_type == 'CitationRecord':
                continue
            item_type = i_type
            break
        if item_type is None:
            return {'response': "Could not retrieve full text of the paper: %s."%(paper_id),
                "data": {'mermaid_code': None, 'run': run_metadata} }

        # 1. Build LangChain elements
        pts = PromptTemplateRegistry()
        
        pts.load_prompts_from_yaml('protocol_extraction.yaml')
        pt = pts.get_prompt_template('protocol diagram extraction').generate_chat_prompt_template()
        extract_lcel = pt | self.llm | MermaidExtractionOutputParser()
        
        # 2. Run through all available sections of the paper and identify only those that are predominantly methods sections.
        start = datetime.now()
        fragments = [f.content for f in self.db.list_fragments_for_paper(paper_id, item_type, fragment_types=['section'])]
        on_off = False
        text = ''
        for t in fragments:
            l1 = t.split('\n')[0].lower()
            if 'method' in l1:
                on_off = True
            elif 'results' in l1 or 'discussion' in l1 or 'conclusion' in l1 or 'acknowledgements' in l1 \
                    or 'references' in l1 or 'supplementary' in l1 or 'appendix' in l1 or 'introduction' in l1 or 'abstract' in l1 or 'cited' in l1:
                on_off = False
            if on_off:
                if len(text) > 0:
                    text += '\n\n'
                text += t

        if len(text) == 0:
            return {'response': "No text generated for the paper: %s."%(paper_id),
                "data": {'mermaid_code': None, 'run': run_metadata} }

        # 4. Assemble chain input
        s1 = {'section_text': text}
        
        # 5. Run the chain with a MermaidExtractionOutputParser 
        output = None
        output = extract_lcel.invoke(s1)#, config={'callbacks': [ConsoleCallbackHandler()]})
        total_execution_time = datetime.now() - start

        if output is None:
            return {'response': "attempted and failed protocol extraction for an experiment from %s."%(paper_id),
                "data": None, 
                'run': run_metadata}
        
        return {'response': "completed protocol extraction for an experiment from %s."%(paper_id),
                "data": output, 
                'run': run_metadata}

# %% ../../nbs/tools/23_protocol_extraction_tool.ipynb 7
class ProcotolEntitiesExtractionTool(BaseProtocolExtractionTool):
    '''Extracts all entities used in a protocol.'''
    name = 'protocol_entities_extraction'
    description = 'Extracts all entities used in a protocol.'

    def _run(self, paper_id):
        '''Extracts all entities used in a protocol.'''

        if self.db.session is None:
            session_class = sessionmaker(bind=self.db.engine)
            self.db.session = session_class()

        # Introspect the class name of the llm model for notes and logging
        llm_class_name = self.llm.__class__.__name__

        run_metadata = {
            'tool': self.__class__.__name__,
            'doi': paper_id,
            'llm_class': llm_class_name}

        # 0. Use the first available full text item type
        item_types = set()
        item_type = None
        for i in self.db.list_items_for_expression(paper_id):
            item_types.add(i.type)
        for i_type in item_types:
            if i_type == 'CitationRecord':
                continue
            item_type = i_type
            break
        if item_type is None:
            return {'response': "Could not retrieve full text of the paper: %s."%(paper_id),
                "data": None, 
                'run': run_metadata}

        # 1. Build LangChain elements
        pts = PromptTemplateRegistry()
        
        pts.load_prompts_from_yaml('protocol_extraction.yaml')
        pt = pts.get_prompt_template('entity extraction').generate_chat_prompt_template()
        parser = JsonOutputParser()

        extract_lcel = pt | self.llm | parser
        
        # 2. Use heuristics to find the start of the methods section and run through until you find the next top-level section
        # Very ugly hack, need to update based on better reading of section headings
        start = datetime.now()
        fragments = [f.content for f in self.db.list_fragments_for_paper(paper_id, item_type, fragment_types=['section'])]
        on_off = False
        text = ''
        for t in fragments:
            l1 = t.split('\n')[0].lower()
            if 'method' in l1:
                on_off = True
            elif 'results' in l1 or 'discussion' in l1 or 'conclusion' in l1 or 'acknowledgements' in l1 \
                    or 'references' in l1 or 'supplementary' in l1 or 'appendix' in l1 or 'introduction' in l1 or 'abstract' in l1 or 'cited' in l1:
                on_off = False
            if on_off:
                if len(text) > 0:
                    text += '\n\n'
                text += t

        if len(text) == 0:
            return {'response': "No text extracted for the paper: %s."%(paper_id),
                "data": None, 
                'run': run_metadata} 

        # 4. Assemble chain input
        s1 = {'section_text': text}
        
        # 5. Run the chain with a MermaidExtractionOutputParser 
        output = None
        output = extract_lcel.invoke(s1)#, config={'callbacks': [ConsoleCallbackHandler()]})
        total_execution_time = datetime.now() - start

        if output is None:
            return {'response': "attempted and failed to list entitles for proctocol from %s."%(paper_id),
                "data": None,
                'run': run_metadata}
        
        return {'response': "completed list of entitles for proctocol from %s."%(paper_id),
                "data": output, 
                'run': run_metadata}

# %% ../../nbs/tools/23_protocol_extraction_tool.ipynb 8
class ProcotolProcessesExtractionTool(BaseProtocolExtractionTool):
    '''Extracts all processes used in a protocol.'''
    name = 'protocol_processes_extraction'
    description = 'Extracts all processes used in a protocol.'

    def _run(self, paper_id):
        '''Extracts all processes used in a protocol.'''

        if self.db.session is None:
            session_class = sessionmaker(bind=self.db.engine)
            self.db.session = session_class()

        # Introspect the class name of the llm model for notes and logging
        llm_class_name = self.llm.__class__.__name__

        run_metadata = {
            'tool': self.__class__.__name__,
            'doi': paper_id,
            'llm_class': llm_class_name}

        # 0. Use the first available full text item type
        item_types = set()
        item_type = None
        for i in self.db.list_items_for_expression(paper_id):
            item_types.add(i.type)
        for i_type in item_types:
            if i_type == 'CitationRecord':
                continue
            item_type = i_type
            break
        if item_type is None:
            return {'response': "Could not retrieve full text of the paper: %s."%(paper_id),
                "data": {'entities': None, 'run': run_metadata} }

        # 1. Build LangChain elements
        pts = PromptTemplateRegistry()
        
        pts.load_prompts_from_yaml('protocol_extraction.yaml')
        pt = pts.get_prompt_template('process extraction').generate_chat_prompt_template()
        parser = JsonOutputParser()

        extract_lcel = pt | self.llm | parser
        
        # 2. Use heuristics to find the start of the methods section and run through until you find the next top-level section
        # Very ugly hack, need to update based on better reading of section headings
        start = datetime.now()
        fragments = [f.content for f in self.db.list_fragments_for_paper(paper_id, item_type, fragment_types=['section'])]
        on_off = False
        text = ''
        for t in fragments:
            l1 = t.split('\n')[0].lower()
            if 'method' in l1:
                on_off = True
            elif 'results' in l1 or 'discussion' in l1 or 'conclusion' in l1 or 'acknowledgements' in l1 \
                    or 'references' in l1 or 'supplementary' in l1 or 'appendix' in l1 or 'introduction' in l1 or 'abstract' in l1 or 'cited' in l1:
                on_off = False
            if on_off:
                if len(text) > 0:
                    text += '\n\n'
                text += t

        if len(text) == 0:
            return {'response': "No text extracted for the paper: %s."%(paper_id),
                "data": {'list_of_answers': None, 'run': run_metadata} }

        # 4. Assemble chain input
        s1 = {'section_text': text}
        
        # 5. Run the chain with a MermaidExtractionOutputParser 
        output = None
        output = extract_lcel.invoke(s1)#, config={'callbacks': [ConsoleCallbackHandler()]})
        total_execution_time = datetime.now() - start

        if output is None:
            return {'response': "attempted and failed to list entitles for proctocol from %s."%(paper_id),
                "data": None, 
                'run': run_metadata} 
        
        return {'response': "completed list of entitles for proctocol from %s."%(paper_id),
                "data": output, 
                'run': run_metadata}
