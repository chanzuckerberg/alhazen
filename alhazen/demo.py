# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_demo.ipynb.

# %% auto 0
__all__ = ['Input', 'Output', 'AlhazenDemo']

# %% ../nbs/02_demo.ipynb 2
import os
import pandas as pd

from .core import PromptTemplateRegistry, get_langchain_llm, get_langchain_embeddings, GGUF_LOOKUP_URL, MODEL_TYPE
import alhazen.utils.jats_text_extractor as te 
from .utils.pdf_research_article_text_extractor import PyMuPDFBlockLoader, PyMuPDFBlockParser, PyMuPDFBlock

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import gradio as gr

from InstructorEmbedding import INSTRUCTOR 

from importlib_resources import files

from langchain.agents import AgentExecutor, load_tools
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import JSONAgentOutputParser
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import AnalyzeDocumentChain,  RetrievalQA, RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders.pdf import PyMuPDFLoader
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.document_loaders import UnstructuredFileLoader
from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import load_prompt, PromptTemplate
from langchain.schema.vectorstore import VectorStoreRetriever
from langchain.text_splitter import NLTKTextSplitter, CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.tools.render import render_text_description, render_text_description_and_args
from langchain.vectorstores import Chroma

from langchain.pydantic_v1 import BaseModel

from langserve import add_routes

from pathlib import Path

import re
import requests


# %% ../nbs/02_demo.ipynb 3
# We need to add these input/output schemas because the current AgentExecutor
# is lacking in schemas.
class Input(BaseModel):
    input: str

class Output(BaseModel):
    output: str     

class AlhazenDemo:
    '''Systems for tool-based agent forming the core of the Alzhazen system.'''

    def __init__(self, 
                home_dir, 
                model_type=MODEL_TYPE.Ollama,
                llm_name='llama2:70b'):
        
        self.home_dir = home_dir
        if home_dir[-1:] != '/':
            home_dir += '/'
        self.change_directory(self.home_dir)
        
        self.tools = load_tools(["ddg-search", "pubmed", "arxiv"])

        pts = PromptTemplateRegistry()
        pts.load_prompts_from_yaml('alhazen_base.yaml')
        if model_type == MODEL_TYPE.Ollama:
            self.prompt_template = pts.get_prompt_template('alhazen tools').generate_llama2_prompt_template()
        else:
            self.prompt_template = pts.get_prompt_template('alhazen tools').generate_prompt_template()
        self.prompt_template = self.prompt_template.partial(
            tools=render_text_description_and_args(self.tools),
            tool_names=", ".join([t.name for t in self.tools]),
        )

        self.llm = get_langchain_llm(model_type, llm_name)
        self.llm_with_stop = self.llm.bind(stop=["\nObservation"])

        self.agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_log_to_str(x["intermediate_steps"]),
            }
            | self.prompt_template
            | self.llm_with_stop
            | JSONAgentOutputParser()
        )

        self.agent_executor = AgentExecutor(
                agent=self.agent, 
                tools=self.tools, 
                verbose=True)
        
        self.app = self.setup_langserve()

    def change_directory(self, doc_dir):
        if doc_dir[-1:] != '/':
            doc_dir += '/'
        file_list = []
        dir_list = []
        with os.scandir(doc_dir) as it:
            for entry in it:
                suffix = Path(entry.path).suffix
                if entry.is_file():
                    if suffix in ['.pdf', '.PDF', '.txt', '.TXT', '.xml', '.XML', '.nxml', '.NXML']:
                        file_list.append(entry.name)
                elif entry.is_dir():
                    dir_list.append(entry.name)
        file_list.sort()
        dir_list.sort()

        # insert '..' into dir_list
        dir_list.insert(0, '..')

        self.home_dir = doc_dir
        self.folder_df = pd.DataFrame(dir_list, columns=['folder'])
        self.file_df = pd.DataFrame(file_list, columns=['file'])
        return (doc_dir, self.folder_df, self.file_df)

    def setup_langserve(self):

        app = FastAPI(
            title="Alhazen Server",
            version="0.0.1",
            description="An api server using Langchain's Runnable interfaces for Alhazen",
        )

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"],
        )

        # Adds routes to the app for using the chain under:
        # /invoke
        # /batch
        # /stream
        add_routes(app, self.agent_executor.with_types(input_type=Input, output_type=Output))

        return app

    def run_langserve(self, port=8080):
        import uvicorn
        uvicorn.run(self.app, host="localhost", port=port)
    
    def run_gradio(self):

        def add_text(history, text):
            #print('add_text: history: %s, text: %s'%(history, text))
            history = history + [(text, None)]
            return history, gr.Textbox(value="", interactive=False)

        def select_dir(evt: gr.SelectData):
            new_dir = self.home_dir + '/' + evt.value      
            if evt.value == '..':
                new_dir = str(Path(self.home_dir).parent)
            print('select_dir: %s'%(new_dir))
            return self.change_directory(new_dir)
            
        def select_file(evt: gr.SelectData):
            file_path = self.home_dir + '/' + evt.value              
            return file_path, []
            
        def clear_chat(history):
            return []

        def bot(history):
            #print('bot: history: %s'%(history))
            # prompt to send to the agent is the last message from the user
            input = history[-1][0]
            response = self.agent_executor.invoke(
                {"input": input}
            )
            print('RESPONSE: %s'%(str(response)))
            history[-1][1] = str(response.get('result','No answer found'))
            print('WHOLE HISTORY: %s'%(history))
            return history

        with gr.Blocks() as demo:
            with gr.Tab("Full Text Documents"):
                with gr.Row():
                    with gr.Column():
                        doc_dir = gr.Textbox(show_label=False, lines=1, value=self.home_dir, interactive=False)
                        with gr.Row():
                            directories = gr.DataFrame(show_label=False, value=self.folder_df, interactive=False)
                            files = gr.DataFrame(show_label=False, value=self.file_df, interactive=False)
                    doc_text = gr.HTML(label="File Contents")
            
            with gr.Tab("Chat"):
                chatbot = gr.Chatbot(
                    [],
                    elem_id="chatbot",
                    bubble_full_width=False,
                    #avatar_images=(None, files(alhazen_resources).joinpath('alhazen.png'))
                )
                with gr.Row():
                    txt = gr.Textbox(
                        scale=4,
                        show_label=False,
                        placeholder="Enter text and press enter, or upload files",
                        container=False,
                    )
                    clear_btn = gr.Button("Clear")

            directories.select(select_dir, None, [doc_dir, directories, files], queue=False )   
            files.select(select_file, None, [doc_text, chatbot], queue=False )
            txt_msg = txt.submit(add_text, [chatbot, txt], [chatbot, txt], queue=False).then(bot, chatbot, chatbot)
            txt_msg.then(lambda: gr.Textbox(interactive=True), None, [txt], queue=False)                
            clear_btn.click(clear_chat, [], [chatbot], queue=False)
                
        demo.queue()
        demo.launch()

