# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/tools/22_metadata_extraction_tool.ipynb.

# %% auto 0
__all__ = ['MetadataExtractionToolSchema', 'BaseMetadataExtractionTool', 'MetadataExtraction_EverythingEverywhere_Tool',
           'MetadataExtraction_MethodsSectionOnly_Tool', 'MetadataExtraction_RAGOnSections_Tool',
           'SimpleExtractionWithRAGToolSchema', 'SimpleExtractionWithRAGTool']

# %% ../../nbs/tools/22_metadata_extraction_tool.ipynb 3
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
import tiktoken
from urllib.request import urlopen
from urllib.parse import quote_plus, quote, unquote
import uuid
import yaml

# %% ../../nbs/tools/22_metadata_extraction_tool.ipynb 4
class MetadataExtractionToolSchema(BaseModel):
    paper_id: str = Field(description="the doi of the paper being analyzed, must start with the string 'doi:'")
    extraction_type: str = Field(description="This is the name of the type of extraction and must be one of the following strings: ['cryoet']")
    run_label: Optional[str] = Field(description="This is a label that will be used to identify the run of the metadata extraction tool in the database.")

class BaseMetadataExtractionTool(BaseTool, AlhazenToolMixin):
    '''Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'''
    name = 'metadata_extraction'
    description = 'Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'
    args_schema = MetadataExtractionToolSchema
    return_direct:bool = True
    examples = {}

    def _run(self, paper_id, extraction_type):
        '''Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'''
        raise NotImplementedError('This method must be implemented by a subclass.')
    
    def compile_answers(self, spec, data_file_path):
        '''Compiles the answers to the metadata extraction questions into a single JSON object.'''
        
        pts = PromptTemplateRegistry()
        pts.load_prompts_from_yaml('metadata_extraction.yaml')
        prompt_elements_yaml = files(prompt_elements).joinpath('metadata_extraction.yaml').read_text()
        prompt_elements_dict = yaml.safe_load(prompt_elements_yaml).get(spec)
        metadata_specs = prompt_elements_dict.get('metadata specs',[])
        dataset_publication_path = prompt_elements_dict['dataset_publication_path']
        
        # walk over the directory tree underneath data_file_path
        # and compile the answers to the metadata extraction questions
        # for each file in the directory tree
        yaml_files = []
        tsv_files = []
        for root, dirs, file_list in os.walk(data_file_path):
            for file in file_list:
                if file.endswith(".yaml"):
                    yaml_files.append((root, file))
                if file.endswith(".tsv"):
                    tsv_files.append((root, file))

        self.examples = {} 
        for root, file in yaml_files:
            with open(os.path.join(root, file), 'r') as f:
                d = yaml.safe_load(f)
                for q in metadata_specs:
                    path = q.get('path')
                    dois = jmespath.search(dataset_publication_path, d).split(',')             
                    answer = jmespath.search(path, d)
                    if answer is None:
                        answer = []
                    else:
                        if not isinstance(answer, list):
                            answer = [answer]
                        else:
                            answer = list(set(answer))
                    for doi in dois:
                        if doi[0:4] != 'doi:' or len(answer) == 0:
                            continue
                        self.examples[q.get('name')][doi.strip()] = list(set(answer))

        for root, file in tsv_files:
            df = pd.read_csv(os.path.join(root, file), sep='\t')
            for i, row in df.iterrows():
                doi = row.doi
                if doi[0:4] != 'doi:':
                    doi = 'doi:'+doi
                for q in metadata_specs:
                    if self.examples.get(q.get('name'), None) is None:
                        self.examples[q.get('name')] = {}
                    if doi not in self.examples.get(q.get('name'), []):
                        self.examples[q.get('name')][doi] = []
                    if q.get('name') in list(row.keys()):
                        v = str(row[str(q.get('name'))])
                        if v == v and v != 'nan':
                            self.examples[q.get('name')][doi].append(str(row[str(q.get('name'))]))
        
        for q in self.examples:
            for doi in self.examples[q]:
                self.examples[q][doi] = ', '.join(sorted(set(self.examples[q][doi])))

    def write_answers_as_notes(self, extraction_type, data_file_path): 
        dois = sorted(list(set([doi for q in self.examples for doi in self.examples[q]])))
        for doi in dois:
            ske = self.db.session.query(SKE) \
                .filter(SKE.id == doi).first() 
            if ske is None:
                continue
            content = {q:self.examples[q].get(doi) for q in self.examples}
            n = Note(
                id=uuid.uuid4().hex[0:10],
                type='MetadataExtractionNote', 
                name = extraction_type+'__'+doi+'__gold',
                provenance='gold standard data loaded from '+data_file_path,
                content=json.dumps(content, indent=4), 
                creation_date=datetime.now(), 
                format='json')
            n.is_about.append(ske)
            self.db.session.add(n)
            self.db.session.flush()
        self.db.session.commit()

    def read_metadata_extraction_notes(self, paper_id, extraction_type, run_label = 'test'):    
        l = []
        q = self.db.session.query(N) \
            .filter(N.id == NIA.Note_id) \
            .filter(NIA.is_about_id == paper_id) \
            .filter(N.type == 'MetadataExtractionNote') \
            .filter(N.name.like(extraction_type+'_%_'+run_label)) 

        for n in q.all():
            tup = json.loads(n.content)
            tup['doi'] = paper_id
            tup['extraction_type'] = extraction_type
            tup['run_label'] = run_label
            #deets = json.loads(n.provenance)
            #tup['tool_name'] = deets.get('tool')
            #tup['llm_name'] = deets.get('llm_class')
            #tup['llm_desc'] = deets.get('llm_desc')  
            #tup['variable'] = deets.get('variable')
            l.append(tup)

        return l 

    def report_metadata_extraction_for_collection(self, collection_id, extraction_type, run_label = 'test'):    
        l = []
        q = self.db.session.query(N,SKE) \
            .filter(N.id == NIA.Note_id) \
            .filter(NIA.is_about_id == SKE.id) \
            .filter(SKC_HM.has_members_id == SKE.id) \
            .filter(SKC_HM.ScientificKnowledgeCollection_id == collection_id) \
            .filter(N.type == 'MetadataExtractionNote') \
            .filter(N.name.like(extraction_type+'_%_'+run_label)) 

        for n, ske in q.all():
            tup = json.loads(n.content)
            tup['doi'] = ske.id
            tup['reference'] = ske.content
            tup['extraction_type'] = extraction_type
            tup['run_label'] = run_label
            #deets = json.loads(n.provenance)
            #tup['tool_name'] = deets.get('tool')
            #tup['llm_name'] = deets.get('llm_class')
            #tup['llm_desc'] = deets.get('llm_desc')  
            #tup['variable'] = deets.get('variable')
            l.append(tup)
        
        df = pd.DataFrame(l)
        return df

# %% ../../nbs/tools/22_metadata_extraction_tool.ipynb 6
class MetadataExtraction_EverythingEverywhere_Tool(BaseMetadataExtractionTool):
    '''Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'''
    name = 'metadata_extraction'
    description = 'Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'

    def _run(self, paper_id, extraction_type, run_label='test'):
        '''Runs the metadata extraction pipeline over a specified paper.'''

        if self.db.session is None:
            session_class = sessionmaker(bind=self.db.engine)
            self.db.session = session_class()

        ske = self.db.session.query(SKE) \
                .filter(SKE.id.like('%'+paper_id+'%')).first()    

        # Introspect the class name of the llm model for notes and logging
        llm_class_name = self.llm.__class__.__name__
        llm_model_desc = str(self.llm)

        run_metadata = {
            'tool': self.__class__.__name__,
            'extraction_type': extraction_type,
            'doi': paper_id,
            'llm_class': llm_class_name,
            'llm_desc': llm_model_desc}

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
            return {'answer': "Could not retrieve full text of the paper: %s."%(paper_id),
                "data": {'list_of_answers': None, 'run': run_metadata} }

        # 1. Build LangChain elements
        pts = PromptTemplateRegistry()
        
        pts.load_prompts_from_yaml('metadata_extraction.yaml')
        prompt_elements_yaml = files(prompt_elements).joinpath('metadata_extraction.yaml').read_text()
        prompt_elements_dict = yaml.safe_load(prompt_elements_yaml).get(extraction_type)
        method_goal = prompt_elements_dict['method goal']
        methodology = prompt_elements_dict['methodology']
        metadata_specs = prompt_elements_dict.get('metadata specs',[])
        metadata_extraction_prompt_template = pts.get_prompt_template('metadata extraction (all questions, whole paper)').generate_chat_prompt_template()
        extract_lcel = metadata_extraction_prompt_template | self.llm | JsonEnclosedByTextOutputParser()
        
        # 2. Run through all available sections of the paper and identify only those that are predominantly methods sections.
        start = datetime.now()
        text = '\n\n'.join([f.content for f in self.db.list_fragments_for_paper(paper_id, item_type, fragment_types=['section'])])

        if len(text) == 0:
            return {'answer': "Could not retrieve full text of the paper: %s."%(paper_id),
                "data": {'list_of_answers': None, 'run': run_metadata} }

        # 3. Compile the extraction questions
        question_text_list = [("%d. %s Record this value in the '%s' field of the output.")
                                %(i+1, spec.get('spec'), spec.get('name')) 
                                for i, spec in enumerate(metadata_specs)]
        questions_output_specification = '\n'.join(question_text_list)
        questions_output_specification += '\nGenerate only JSON formatted output with %d fields:\n'%(len(metadata_specs))
        questions_output_specification += ", ".join([spec.get('name') for spec in metadata_specs])

        # 4. Assemble chain input
        s1 = {'section_text': text,
                'methodology': methodology,
                'method_goal': method_goal,
                'questions_output_specification': questions_output_specification}
        
        # 5. Run the chain with a JsonEnclosedByTextOutputParser 
        output = None
        attempts = 0
        full_answer = []
        output = extract_lcel.invoke(s1, config={'callbacks': [ConsoleCallbackHandler()]})
        total_execution_time = datetime.now() - start
        time_per_variable = total_execution_time / len(metadata_specs)

        if output is None:
            return {'answer': "attempted and failed metadata extraction for an experiment of type '%s' from %s."%(methodology, paper_id),
                "data": {'list_of_answers': None, 'run': run_metadata} }
        
        run_metadata['timestamp'] = start.strftime('%Y-%m-%d %H:%M:%S')
        run_metadata['time_taken'] = str(total_execution_time)
        run_name = extraction_type+'__'+paper_id+'__'+run_label
        n = Note(
            id=uuid.uuid4().hex[0:10],
            type='MetadataExtractionNote', 
            name=run_name,
            provenance=json.dumps(run_metadata, indent=4),
            content=json.dumps(output, indent=4), 
            creation_date=datetime.now(), 
            format='json')

        n.is_about.append(ske)
        self.db.session.add(n)
        self.db.session.flush()
                    
        # commit the changes to the database
        self.db.session.commit()
        
        return {'answer': "completed metadata extraction for an experiment of type '%s' from %s."%(methodology, paper_id),
                "data": output, 
                'run': run_metadata}

# %% ../../nbs/tools/22_metadata_extraction_tool.ipynb 7
class MetadataExtraction_MethodsSectionOnly_Tool(BaseMetadataExtractionTool):
    '''Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'''
    name = 'metadata_extraction'
    description = 'Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'

    def _run(self, paper_id, extraction_type, run_label='test'):
        '''Runs the metadata extraction pipeline over a specified paper.'''

        if self.db.session is None:
            session_class = sessionmaker(bind=self.db.engine)
            self.db.session = session_class()

        ske = self.db.session.query(SKE) \
                .filter(SKE.id.like('%'+paper_id+'%')).first()    

        # 0. Use the first available full text item type
        item_types = set()
        for i in self.db.list_items_for_expression(paper_id):
            item_types.add(i.type)
        for i_type in item_types:
            if i_type == 'CitationRecord':
                continue
            item_type = i_type
            break

        # Introspect the class name of the llm model for notes and logging
        llm_class_name = self.llm.__class__.__name__
        llm_model_desc = str(self.llm)

        run_metadata = {
            'tool': self.__class__.__name__,
            'doi': paper_id,
            'llm_class': llm_class_name,
            'llm_desc': llm_model_desc}

        # 1. Build LangChain elements
        pts = PromptTemplateRegistry()
        
        #pts.load_prompts_from_yaml('document_structure.yaml')
        #section_classifier_prompt_template = pts.get_prompt_template('full text paper section classification').generate_chat_prompt_template()
        #section_classifier_lcel = section_classifier_prompt_template | self.slm | JsonEnclosedByTextOutputParser()

        pts.load_prompts_from_yaml('metadata_extraction.yaml')
        prompt_elements_yaml = files(prompt_elements).joinpath('metadata_extraction.yaml').read_text()
        prompt_elements_dict = yaml.safe_load(prompt_elements_yaml).get(extraction_type)
        method_goal = prompt_elements_dict['method goal']
        methodology = prompt_elements_dict['methodology']
        metadata_specs = prompt_elements_dict.get('metadata specs',[])
        metadata_extraction_prompt_template = pts.get_prompt_template('metadata extraction (all questions, whole paper)').generate_chat_prompt_template()
        extract_lcel = metadata_extraction_prompt_template | self.llm | JsonEnclosedByTextOutputParser()
                
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
            return {'answer': "Could not retrieve full text of the paper: %s."%(paper_id),
                "data": {'list_of_answers': None, 'run': run_metadata} }

        # 3. Compile the extraction questions
        question_text_list = [("%d. %s Record this value in the '%s' field of the output.")
                                %(i+1, spec.get('spec'), spec.get('name')) 
                                for i, spec in enumerate(metadata_specs)]
        questions_output_specification = '\n'.join(question_text_list)
        questions_output_specification += '\nGenerate only JSON formatted output with %d fields:\n'%(len(metadata_specs))
        questions_output_specification += ", ".join([spec.get('name') for spec in metadata_specs])

        # 4. Assemble chain input
        s1 = {'section_text': text,
                'methodology': methodology,
                'method_goal': method_goal,
                'questions_output_specification': questions_output_specification}
        
        # 5. Run the chain with a JsonEnclosedByTextOutputParser 
        output = None
        attempts = 0
        full_answer = []
        output = extract_lcel.invoke(s1, config={'callbacks': [ConsoleCallbackHandler()]})
        total_execution_time = datetime.now() - start
        time_per_variable = total_execution_time / len(metadata_specs)

        if output is None:
            return {'answer': "attempted and failed metadata extraction for an experiment of type '%s' from %s."%(methodology, paper_id),
                "data": {'list_of_answers': None, 'run': run_metadata} }

        run_name = extraction_type+'__'+paper_id+'__'+run_label

        n = Note(
            id=uuid.uuid4().hex[0:10],
            type='MetadataExtractionNote', 
            name=run_name,
            provenance=json.dumps(run_metadata, indent=4),
            content=json.dumps(output, indent=4), 
            creation_date=datetime.now(), 
            format='json')
        n.is_about.append(ske)
        self.db.session.add(n)
        self.db.session.flush()
                    
        # commit the changes to the database
        self.db.session.commit()
        
        return {'response': "completed metadata extraction for an experiment of type '%s' from %s."%(methodology, paper_id),
                "data": output, 
                'run': run_metadata} 

# %% ../../nbs/tools/22_metadata_extraction_tool.ipynb 8
class MetadataExtraction_RAGOnSections_Tool(BaseMetadataExtractionTool):
    '''Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'''
    name = 'metadata_extraction'
    description = 'Runs a specified metadata extraction pipeline over a research paper that has been loaded in the local literature database.'
    
    def _run(self, paper_id, extraction_type):
        '''Runs the metadata extraction pipeline over the FullText of a specified paper.'''

        if self.db.session is None:
            session_class = sessionmaker(bind=self.db.engine)
            self.db.session = session_class()

        # 1. Load basic prompts and build vectorstore    
        os.environ['PGVECTOR_CONNECTION_STRING'] = "postgresql+psycopg2:///"+self.db.name
        vectorstore = PGVector.from_existing_index(
                embedding = self.db.embed_model, 
                collection_name = 'ScienceKnowledgeItem_FullText') 
        if paper_id[0:4] != 'doi:':
            paper_id = 'doi:'+paper_id
        retriever = vectorstore.as_retriever(search_kwargs={'filter': {'ske_id': paper_id}})

        pts = PromptTemplateRegistry()
        pts.load_prompts_from_yaml('metadata_extraction.yaml')
        prompt_elements_yaml = files(prompt_elements).joinpath('metadata_extraction.yaml').read_text()
        prompt_elements_dict = yaml.safe_load(prompt_elements_yaml).get(extraction_type)
        method_goal = prompt_elements_dict['method goal']
        methodology = prompt_elements_dict['methodology']
        metadata_specs = prompt_elements_dict.get('metadata specs',[])
        metadata_extraction_prompt_template = pts.get_prompt_template(
            'metadata extraction (RAG over full text snippets)').generate_chat_prompt_template()
        run_name = 'metadata_extraction_' + re.sub(' ','_',extraction_type) + ':' + paper_id

        # 2. Iterate over questions to run extraction pipeline
        full_answer = []
        for i, spec in enumerate(metadata_specs):
            question = spec.get('spec')
            answer_spec = "Record this value in the '%s' field of the output."%(spec.get('name')) 
            answer_spec += '\nGenerate only JSON formatted output with one field\n'
            answer_spec += spec.get('name')

            input = {'question': question,
                'answer_specification': answer_spec,
                'methodology': methodology,
                'method_goal': method_goal}    
            
            qa_chain = (
                RunnableParallel({
                    "question": itemgetter("question"),
                    "context": itemgetter("question") | retriever,
                    "answer_specification": itemgetter("answer_specification"),
                    "methodology": itemgetter("methodology"),
                    "method_goal": itemgetter("method_goal")
                })
                | {
                    "response": metadata_extraction_prompt_template | self.llm | JsonEnclosedByTextOutputParser(),
                    "context": itemgetter("context"),
                }
            )
            
            # 5. Run the chain
            output = qa_chain.invoke(input, config={'callbacks': [ConsoleCallbackHandler()]})
            vname = spec.get('name')
            question = spec.get('spec')
            answer = output.get('response',{}).get(vname) 
            fragment_ids = []
            for skf_id in [d.metadata.get('skf_id') for d in output.get('context', [])]:
                fragment_ids.append(skf_id)
                f = self.db.session.query(skf) \
                    .filter(skf.id == skf_id).first()
                note_content = json.dumps({
                    'question': question,
                    'answer': answer,
                    'variable': vname}, indent=4)
                # add a note to the fragment
                n = Note(id=uuid.uuid4().hex[0:10],
                        type='MetadataExtractionNote__'+extraction_type, 
                        name=run_name+':'+vname,
                        content=note_content, 
                        creation_date=datetime.now(), 
                        format='json')
                n.is_about.append(f)
                self.db.session.add(n)
                self.db.session.flush()
            self.db.session.commit()
            full_answer.append({'variable_name': vname, 'question': question, 'fragment_ids': fragment_ids})
        
        return {'response': "completed metadata extraction for an experiment of type '%s' from %s."%(methodology, paper_id),
                "data": {'list_of_answers': full_answer, 'run_name': run_name} }

# %% ../../nbs/tools/22_metadata_extraction_tool.ipynb 9
class SimpleExtractionWithRAGToolSchema(BaseModel):
    paper_id: str = Field(description="The digitial object identifier (doi) of the paper being analyzed.")
    variable_name: str = Field(description="This is the variable that the question is attempting to extract from the paper.")
    question: str = Field(description="This is the question that must be answered to perform the extraction.")

class SimpleExtractionWithRAGTool(BaseTool, AlhazenToolMixin):
    '''Performs simple information extraction from a specified research paper from the database.'''
    name = 'simple_extraction'
    description = 'Performs simple information extraction from a specified research paper from the database.'
    args_schema = SimpleExtractionWithRAGToolSchema
    
    def _run(self, paper_id, variable_name, question ):
        '''Runs the simple extraction pipeline over the FullText of a specified paper.'''

        if self.db.session is None:
            session_class = sessionmaker(bind=self.db.engine)
            self.db.session = session_class()

        # 1. Load basic prompts and build vectorstore    
        os.environ['PGVECTOR_CONNECTION_STRING'] = "postgresql+psycopg2:///"+self.db.name
        vectorstore = PGVector.from_existing_index(
                embedding = self.db.embed_model, 
                collection_name = 'ScienceKnowledgeItem_FullText') 
        if paper_id[0:4] != 'doi:':
            paper_id = 'doi:'+paper_id
        retriever = vectorstore.as_retriever(search_kwargs={'filter': {'ske_id': paper_id}})

        pts = PromptTemplateRegistry()
        pts.load_prompts_from_yaml('metadata_extraction.yaml')
        simple_extraction_prompt_template = pts.get_prompt_template('simple extraction').generate_chat_prompt_template()

        # 2. Iterate over questions to run extraction pipeline
        full_answer = []
        answer_spec = "Record this value in the '%s' field of the output."%(variable_name) 
        answer_spec += '\nGenerate only JSON formatted output.' 

        input = {'question': question, 'answer_specification': answer_spec}    
            
        qa_chain = (
            RunnableParallel({
                "question": itemgetter("question"),
                "context": itemgetter("question") | retriever,
                "answer_specification": itemgetter("answer_specification"),
            })
            | {
                "response": simple_extraction_prompt_template | self.llm | JsonEnclosedByTextOutputParser(),
                "context": itemgetter("context"),
            }
        )
            
        # 5. Run the chain
        output = qa_chain.invoke(input, config={'callbacks': [ConsoleCallbackHandler()]})
        answer = output.get('response',{}).get(variable_name) 
        fragment_ids = []
        for skf_id in [d.metadata.get('skf_id') for d in output.get('context', [])]:
            fragment_ids.append(skf_id)
            f = self.db.session.query(skf) \
                .filter(skf.id == skf_id).first()
            note_content = json.dumps({
                'question': question,
                'answer': answer,
                'variable': variable_name}, indent=4)
            # add a note to the fragment
            n = Note(id=uuid.uuid4().hex[0:10],
                    type='NoteAboutFragment', 
                    name=paper_id+':'+variable_name,
                    content=note_content, 
                    creation_date=datetime.now(), 
                    format='json')
            n.is_about.append(f)
            self.db.session.add(n)
            self.db.session.flush()
        self.db.session.commit()
        full_answer = {'variable_name': variable_name, 'question': question, 'fragment_ids': fragment_ids}
    
        return {'response': "I answered this question: `%s` concerning this variable: `%s` from %s."%(question, variable_name, paper_id),
                "data": {'answer': full_answer }}
