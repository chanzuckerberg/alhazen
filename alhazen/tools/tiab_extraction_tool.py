# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/tools/27_tiab_extraction_tool.ipynb.

# %% auto 0
__all__ = ['TitleAbstractExtractionToolSchema', 'BaseTitleAbstractExtractionTool', 'TitleAbstractExtraction_OneDocAtATime_Tool']

# %% ../../nbs/tools/27_tiab_extraction_tool.ipynb 3
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

# %% ../../nbs/tools/27_tiab_extraction_tool.ipynb 4
class TitleAbstractExtractionToolSchema(BaseModel):
    collection_id: str = Field(description="the id of the collection being analyzed.")
    domain: str = Field(description="This is the name of the domain of study. It is typically very broad.")
    extraction_type: str = Field(description="This is the name of the type of extraction to be performed.  It is used to select the appropriate pipeline for the extraction.  It is also used to select the appropriate prompt for the extraction.")
    repeat_run: Optional[bool] = Field(description="Whether or not to repeat the classification task if it has been performed before. Defaults to False.")
    
class BaseTitleAbstractExtractionTool(BaseTool, AlhazenToolMixin):
    '''Runs a specified document classification pipeline over papers in a collection.'''
    name = 'tiab_classification'
    description = 'Runs a specified document classification pipeline over papers in a collection.'
    args_schema = TitleAbstractExtractionToolSchema
    return_direct:bool = True
    prompt_name:str = 'binary methods paper'
    examples = {}

    def _run(self, collection_id, domain, extraction_type, repeat_run=False):
        '''Runs a specified information extraction pipeline over papers in a collection.'''
        raise NotImplementedError('This method must be implemented by a subclass.')

# %% ../../nbs/tools/27_tiab_extraction_tool.ipynb 5
class TitleAbstractExtraction_OneDocAtATime_Tool(BaseTitleAbstractExtractionTool):
    '''Runs a specified document classification pipeline over papers in a collection.'''
    name = 'tiab_one_doc_classification'
    description = 'Runs a specified document classification pipeline over papers in a collection by running a simple classifier over the text of each title + abstract.'

    def _run(self, collection_id, extraction_type, repeat_run=False):
        '''Runs a document classification pipeline over papers in a collection one paper at a time.'''
    
        output_list = []

        # Introspect the class name of the llm model for notes and logging
        llm_class_name = self.llm.__class__.__name__

        run_name = self.__class__.__name__+'__'+re.sub(' ','_',extraction_type)+'__'+collection_id+'__'+llm_class_name

        exp_q = self.db.session.query(SKE) \
                .filter(SKC_HM.has_members_id == SKE.id) \
                .filter(SKC_HM.ScientificKnowledgeCollection_id == str(collection_id)) \
                .filter(SKE.id == SKE_HR.ScientificKnowledgeExpression_id) \
                .filter(SKE_HR.has_representation_id == SKI.id) \
                .filter(SKI.type=='CitationRecord') \
                .order_by(desc(SKE.publication_date))
        for e in tqdm(exp_q.all()):
        
            # skip expressions if they have this type of note already.
            if repeat_run is False: 
                repeat_flag = False
                for n in self.db.read_notes_about_x(e):
                    if n.type == 'TiAbExtractionNote__'+extraction_type:
                        repeat_flag = True
                        break
                if repeat_flag:
                    continue

            # 1. Build LangChain elements
            pts = PromptTemplateRegistry()
            pts.load_prompts_from_yaml('tiab_prompts.yaml')

            prompt_elements_yaml = files(prompt_elements).joinpath('metadata_extraction.yaml').read_text()
            prompt_elements_dict = yaml.safe_load(prompt_elements_yaml).get(extraction_type)
            extraction_specs = prompt_elements_dict.get('tiab metadata specs',[])

            tiab_extraction_prompt_template = pts.get_prompt_template('multiquestion tiab extraction').generate_chat_prompt_template()
            extract_lcel = tiab_extraction_prompt_template | self.llm | JsonOutputParser()        
            
            # 2. Run through all available sections of the paper and identify only those that are predominantly methods sections.
            start = datetime.now()
            title, abstract = [f.content for f in self.db.list_fragments_for_paper(e.id, 'CitationRecord')]

            if len(title + abstract) == 0:
                continue

            # 3. Compile the extraction questions
            question_text_list = [("%d. %s Record this value in the '%s' field of the output.")
                                %(i+1, spec.get('spec'), spec.get('name')) 
                                for i, spec in enumerate(extraction_specs)]
            questions_output_specification = '\n'.join(question_text_list)
            questions_output_specification += '\nGenerate only JSON formatted output with %d fields:\n'%(len(extraction_specs))
            questions_output_specification += ", ".join([spec.get('name') for spec in extraction_specs])

            # 4. Assemble chain input
            s1 = {'title': title,
                'abstract': abstract,
                'questions_output_specification': questions_output_specification}
        
            # 4. Run the chain with a JsonEnclosedByTextOutputParser 
            try: 
                output = extract_lcel.invoke(s1)#, config={'callbacks': [ConsoleCallbackHandler()]})
            except Exception as ex:
                # Note that the LLM may raise an exception if it is unable to classify the document.
                print(ex)
                output = "ERROR: Unable to classify document."
                continue
            
            total_execution_time = datetime.now() - start

            output_list.append({'extraction':output, 'paper_id':e.id})
            
            # 5. add a note to the fragment
            if output is not None:

                # Sometime the LLM generates a list. If so, we just take the first item.
                if isinstance(output, list):
                    output = output[0]

            n = Note(
                id=uuid.uuid4().hex[0:10],
                type='TiAbExtractionNote__'+extraction_type, 
                name=run_name+e.id,
                provenance='time_taken: %s'%(str(total_execution_time)),
                content=json.dumps(output, indent=4), 
                creation_date=datetime.now(), 
                format='json')
            self.db.session.add(n)
            n.is_about.append(e)
            self.db.session.commit()
                            
        return {'response': "completed document extraction of type '%s' for collection %s."%(classification_type, collection_id),
                "data": output_list, 
                'run_name': run_name}
