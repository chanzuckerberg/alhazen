# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/tools/26_tiab_mapping_tool.ipynb.

# %% auto 0
__all__ = ['TitleAbstractMappingToolSchema', 'BaseTitleAbstractMappingTool', 'TitleAbstractDiscourseMappingTool']

# %% ../../nbs/tools/26_tiab_mapping_tool.ipynb 3
from ..aliases import *
from ..core import PromptTemplateRegistry
from .basic import AlhazenToolMixin
from ..utils.output_parsers import JsonEnclosedByTextOutputParser
from ..utils.ceifns_db import *
from ..schema_sqla import *
from datetime import datetime
from importlib_resources import files
import jmespath
import json

from langchain.callbacks.tracers import ConsoleCallbackHandler

from langchain_community.embeddings.huggingface import HuggingFaceBgeEmbeddings
from langchain.memory import ConversationBufferMemory
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
from sqlalchemy import create_engine, exists, func, or_, desc
from sqlalchemy.orm import sessionmaker, aliased
from time import time,sleep
import tiktoken
from typing import Optional, Type
from tqdm import tqdm
from urllib.request import urlopen
from urllib.parse import quote_plus, quote, unquote
import uuid
import yaml

# %% ../../nbs/tools/26_tiab_mapping_tool.ipynb 4
class TitleAbstractMappingToolSchema(BaseModel):
    collection_id: str = Field(description="the id of the collection being analyzed.")
    repeat_run: Optional[bool] = Field(description="Whether or not to repeat the classification task if it has been performed before. Defaults to False.")
    run_label: Optional[str] = Field(description="This is a label that will be used to identify the run of the tool in the database. Defaults to 'dev'")

class BaseTitleAbstractMappingTool(BaseTool, AlhazenToolMixin):
    '''Runs a specified document mapping pipeline over papers in a collection.'''
    name = 'tiab_mapping'
    description = 'Runs a specified document mapping pipeline over papers in a collection.'
    args_schema = TitleAbstractMappingToolSchema
    return_direct:bool = True
    
    def _run(self, collection_id, repeat_run=False):
        '''Runs a specified document mapping pipeline over papers in a collection.'''
        raise NotImplementedError('This method must be implemented by a subclass.')

# %% ../../nbs/tools/26_tiab_mapping_tool.ipynb 5
class TitleAbstractDiscourseMappingTool(BaseTitleAbstractMappingTool):
    '''Runs through the text of each title + abstract and split them based on discourse.'''
    name = 'tiab_one_doc_classification'
    description = '''Runs through the text of each title + abstract and split them based on discourse.'''
    
    def _run(self, collection_id, run_label='dev', repeat_run=False):
        '''Runs through the text of each title + abstract and split them based on discourse.'''

        # 1. Build LangChain elements
        pts = PromptTemplateRegistry()
        pts.load_prompts_from_yaml('tiab_prompts.yaml')
        tiab_mapper_prompt_template = pts.get_prompt_template('split_by_discourse').generate_chat_prompt_template()
        mapper_lcel = tiab_mapper_prompt_template | self.llm | JsonOutputParser()        

        output_list = []
        llm_class_name = self.llm.__class__.__name__
        run_metadata = {
            'tool': self.__class__.__name__,
            'mapping_type': 'discourse_tags',
            'llm_class': llm_class_name}

        exp_q = self.db.session.query(SKE) \
                .filter(SKC_HM.has_members_id == SKE.id) \
                .filter(SKC_HM.ScientificKnowledgeCollection_id == str(collection_id)) \
                .filter(SKE.id == SKE_HR.ScientificKnowledgeExpression_id) \
                .filter(SKE_HR.has_representation_id == SKI.id) \
                .filter(SKI.type=='CitationRecord') \
                .filter(or_(SKE.type == 'ScientificPrimaryResearchArticle', SKE.type == 'ScientificPrimaryResearchPreprint')) \
                .order_by(desc(SKE.publication_date))

        for e in tqdm(exp_q.all()):
        
            # skip expressions if they have this type of note already.
            if repeat_run is False: 
                repeat_flag = False
                for n in self.db.read_notes_about_x(e):
                    if n.type == 'TiAbMappingNote__Discourse':
                        repeat_flag = True
                        break
                if repeat_flag:
                    continue

            # 2. Run through all available sections of the paper and identify only those that are predominantly methods sections.
            start = datetime.now()
            title, abstract = [f.content for f in self.db.list_fragments_for_paper(e.id, 'CitationRecord')]

            if len(title + abstract) == 0:
                continue

            # 3. Assemble chain input
            s1 = {'title': title, 'abstract': abstract}
        
            # 4. Run the chain with a JsonEnclosedByTextOutputParser 
            try: 
                output = mapper_lcel.invoke(s1)#, config={'callbacks': [ConsoleCallbackHandler()]})
            except Exception as ex:
                # Note that the LLM may raise an exception if it is unable to classify the document.
                print(ex)
                output = "ERROR: Unable to classify document."
                continue
            
            total_execution_time = datetime.now() - start

            output['paper_id'] = e.id
            output_list.append(output)

            # 5. add a note to the fragment
            run_metadata_1 = run_metadata.copy()
            run_metadata_1['time_taken'] = str(total_execution_time)
            if output is not None:
                n = Note(
                    id=uuid.uuid4().hex[0:10],
                    type='TiAbMappingNote__Discourse', 
                    name=e.id+'__discourse_text_'+run_label,
                    provenance=json.dumps(run_metadata_1, indent=4),
                    content=json.dumps(output, indent=4), 
                    creation_date=datetime.now(), 
                    format='json')
                self.db.session.add(n)
                n.is_about.append(e)
                self.db.session.commit()

        output_list = []
                            
        return {'response': "completed discourse mapping for collection %s."%(collection_id),
                "data": output_list, 
                'run': run_metadata}
