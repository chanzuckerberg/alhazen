# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/24_PaperQA_emulation_tool.ipynb.

# %% auto 0
__all__ = ['skc', 'skc_hm', 'ske', 'ske_hr', 'ski', 'ski_hp', 'skf', 'n', 'skc_hn', 'ske_hn', 'ski_hn', 'skf_hn',
           'PaperQAEmulationToolSchema', 'PaperQAEmulationTool']

# %% ../../nbs/24_PaperQA_emulation_tool.ipynb 3
from ..core import OllamaRunner, PromptTemplateRegistry, get_langchain_llm, get_cached_gguf, \
    get_langchain_embeddings, GGUF_LOOKUP_URL, MODEL_TYPE, load_alhazen_tool_environment, get_langchain_chatmodel
from .basic import AlhazenToolMixin
from ..utils.output_parsers import JsonEnclosedByTextOutputParser
from ..utils.ceifns_db import *
from ..schema_sqla import *
from datetime import datetime
from importlib_resources import files
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
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

import local_resources.prompt_elements as prompt_elements
import local_resources.linkml as linkml
from operator import itemgetter
import os
import re
import regex
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker, aliased
from time import time,sleep
from typing import Optional, Type
from urllib.request import urlopen
from urllib.parse import quote_plus, quote, unquote
import uuid
import yaml

# %% ../../nbs/24_PaperQA_emulation_tool.ipynb 4
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

# %% ../../nbs/24_PaperQA_emulation_tool.ipynb 5
class PaperQAEmulationToolSchema(BaseModel):
    question: str = Field(description="The question to be considered by this workflow.")
    n_sample_size: Optional[int] = Field(description="The number of documents queried from the index to be evaluated for relevance.")
    n_summary_size: Optional[int] = Field(description="The number of documents queried from the index to be used in generating an answer.")
    collection_id: Optional[int] = Field(None, description="The identifier of the collection to be used to answer the question.")

class PaperQAEmulationTool(BaseTool, AlhazenToolMixin):
    '''Write a short essay to answer a scientific question based documents from a preset collection.'''
    name = 'simple_qa_over_papers'
    description = '''Runs a Map-Reduce model where we write a short essay to answer a scientific question based on a set of supporting documents.'''
    args_schema = PaperQAEmulationToolSchema
    return_direct:bool = True
    
    def _run(self, question, n_sample_size=15, n_summary_size=5, collection_id=-1):
        '''Runs the metadata extraction pipeline over a specified paper.'''
        
        DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template='"DOI": "{e_id}","CITATION": "{citation}", "CONTENT":"{page_content}"')
        def _combine_documents(docs):
            m = [{'CONTENT':d.page_content, 'DOI':d.metadata.get('e_id'), "CITATION": d.metadata.get('citation')} for d in docs]
            return json.dumps(m)

        #~~~~~~~~~~~~~~~~~~~~~~
        # 1. Set up environment
        #~~~~~~~~~~~~~~~~~~~~~~
        loc, db_name, model_type, model_name = load_alhazen_tool_environment()

        os.environ['PGVECTOR_CONNECTION_STRING'] = "postgresql+psycopg2:///"+db_name
            
        vectorstore = PGVector.from_existing_index(
                embedding = self.db.embed_model, 
                collection_name = 'ScienceKnowledgeItem') 
        
        # set default values for optional parameters
        retriever = vectorstore.as_retriever(search_kwargs={'k':n_sample_size})
        if collection_id != -1:
            retriever = vectorstore.as_retriever(search_kwargs={'k':n_sample_size, 'filter': {'c_ids': collection_id}})

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 2. Run Map Function - Iterate over 'pages' of Documents returned from vectorstore to generate 
        #                       summaries
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                
        context_build_chain = (
            RunnableParallel({
                "k": itemgetter("k"),
                "question": itemgetter("question"),
                "context": itemgetter("question") | retriever | _combine_documents 
            }
        ))

        pts = PromptTemplateRegistry()
        pts.load_prompts_from_yaml('paperqa_emulation.yaml')
        pt = pts.get_prompt_template('summarize paper set').generate_chat_prompt_template()
        
        summary_chain = (
            RunnableParallel({
                "k": itemgetter("k"),
                "question": itemgetter("question"),
                "summary_length": itemgetter("summary_length"),
                "context": itemgetter("context"),
            })
            | {
                "summary": pt | self.llm | JsonEnclosedByTextOutputParser(),
                "context": itemgetter("context"),
            }
        )

        input = {'question': question, 'summary_length': 1000, 'k':5}    
        out = context_build_chain.invoke(input, config={'callbacks': [ConsoleCallbackHandler()]})
        context = json.loads(out.get('context'))
        citation_lookup = {d.get('DOI'):d.get('CITATION') for d in context}

        page_size = 3
        page_count = int(n_sample_size / page_size)
        summaries = []
        for pg in range(page_count):
            paged_context = []
            paged_doi_lookup = {}
            paged_citation_lookup = {}
            for i,j in enumerate(range(pg*page_size, (pg+1)*page_size)):
                c = {k:context[j][k] for k in context[j] if k!='DOI'}
                c['ID'] = i + 1
                paged_context.append(c)
                paged_citation_lookup[i+1] = context[j]['CITATION']
                paged_doi_lookup[i+1] = context[j]['DOI']
            paged_input = input.copy()
            paged_input['context'] = json.dumps(paged_context)
            out2 = summary_chain.invoke(paged_input, config={'callbacks': [ConsoleCallbackHandler()]})
            summs = out2.get('summary', [])
            if summs:
                for m in out2.get('summary', []):
                    id = m.get('ID')
                    if paged_citation_lookup.get(id):
                        n = {}
                        n['SUMMARY'] = m['SUMMARY']
                        n['RELEVANCE SCORE'] = m['RELEVANCE SCORE']
                        n['CITATION'] = paged_citation_lookup[id]
                        n['DOI'] = paged_doi_lookup[id]
                        summaries.append(n)
                        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 3. Order sumaries in terms of 'RELEVANCE'
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ordered_summaries = []

        # Check to make sure that RELEVANCE SCORES generated by the LLM are integers
        checked_summaries = []
        for s in summaries:
            rel_score = s.get('RELEVANCE SCORE', 'Not Applicable')
            try: 
                check = int(rel_score)
                checked_summaries.append( s )
            except ValueError:
                skip_this = 0

        doi_lookup = {}
        for i, s in enumerate(sorted(checked_summaries, key=lambda x: int(x['RELEVANCE SCORE']), reverse=True)):
            if int(s['RELEVANCE SCORE']) < 7:
                continue
            s['ID'] = i+1
            doi_lookup[i+1] = s.get('DOI')
            ordered_summaries.append({'ID':s.get('ID'),
                                        'CITATION': s.get('CITATION'), 
                                        'SUMMARY': s.get('SUMMARY'), 
                                        'RELEVANCE': s.get('RELEVANCE SCORE')})
            
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 4. Run Reduce Function - Write the synthesis over summaries provided
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        pt2 = pts.get_prompt_template('write synthesis').generate_chat_prompt_template()

        qa_synthesis_chain = (
            RunnableParallel({
                "question": itemgetter("question"),
                "context": itemgetter("context"),
            })
            | {
                "answer": pt2 | self.llm,
                "context": itemgetter("context"),
            }
        )

        input = {'question': question, 'context': ordered_summaries[:n_summary_size]}    
        out3 = qa_synthesis_chain.invoke(input, config={'callbacks': [ConsoleCallbackHandler()]})

        essay = out3.get('answer').content
        essay += "\n\n\nREFERENCES\n" 
        essay += '\n'.join(['[%d] %s (%s)'%(s['ID'],s['CITATION'],doi_lookup[s['ID']]) for s in ordered_summaries[:n_summary_size]])
        
        dois_to_record = [doi_lookup[s['ID']] for s in ordered_summaries[:n_summary_size]]

        if collection_id != 1:
            response = {'report': "I answered this question: `%s` based on content from the collection with id: %s."%(question, collection_id),
                    "data": essay }
        else:
            response = {'report': "I answered this question: `%s` based on all content in our database. "%(question),
                    "data": essay }

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 5. Add Question + Notes to represent the Questions / Answer Generation
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        prov1 = json.dumps([{'action_type': 'user_input', 
                    'action': {'question': question}}])
        q = UserQuestion(id=uuid.uuid4().hex[0:10],
                    content=question,
                    provenance=prov1,
                    format='json',
                    type='NoteAboutCollection')
        self.db.session.add(q)
        prov = json.dumps([{'action_type': self.name, 
                            'action': {'id': id, 
                                       'n_sample_size': n_sample_size, 
                                       'n_summary_size': n_summary_size, 
                                       'collection_id': collection_id,
                                       'question': question}}])            
        n = Note(id=uuid.uuid4().hex[0:10],
                name='skc:%s.counts'%(id),
                content=json.dumps(response),
                provenance=prov,
                format='json',
                type='NoteAboutFragment')
        self.db.session.add(n)
        
        if collection_id != -1:
            c = self.db.session.query(SKC).filter(SKC.id == collection_id).all()[0]
            n.is_about.append(c)
            c.has_notes.append(n)

        q.has_notes.append(n)
        for doi in dois_to_record:
            t, a = self.db.list_fragments_for_paper(doi, 'CitationRecord')
            t.has_notes.append(n)
            a.has_notes.append(n)
        
        self.db.session.commit()

        return response
