# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['PromptTemplateSpec', 'PromptTemplateRegistry', 'load_alhazen_tool_environment', 'lookup_chat_models',
           'lookup_embeddings', 'suppress_stdout_stderr', 'OllamaRunner']

# %% ../nbs/00_core.ipynb 3
import asyncio
import dataclasses
from enum import auto, Enum
from importlib_resources import files

from langchain.schema import SystemMessage, HumanMessage
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.embeddings.llamacpp import LlamaCppEmbeddings
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceBgeEmbeddings
from langchain_community.chat_models.ollama import ChatOllama
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_community.llms.openai import OpenAI
from langchain_community.llms.ollama import Ollama 
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_vertexai import ChatVertexAI

import local_resources.prompts as prompts

import os
import signal
import subprocess
from time import sleep
import torch
from typing import List, Tuple, Any, Dict
import yaml 

# %% ../nbs/00_core.ipynb 4
@dataclasses.dataclass
class PromptTemplateSpec:
    """A class that provides structure for task instructions (to be converted to LangChain PromptTemplates)."""

    # The name of this instruction template
    name: str

    # The description of this instruction template
    description: str

    # System prompts
    system: str

    # Instruction prompts
    instruction: str
    
    # The input variables that this instruction template requires
    input_variables: List[str] = dataclasses.field(default_factory=list)

    # The output variables that this instruction template generates
    output_variables: List[str] = dataclasses.field(default_factory=list)

    def generate_prompt_template(self) -> PromptTemplate:
        return PromptTemplate(
            input_variables=self.input_variables, 
            template=self.system + '\n' +self.instruction
        )

    def generate_llama2_prompt_template(self) -> PromptTemplate:
        return PromptTemplate(
            input_variables=self.input_variables, 
            template='''<s>[INST]
                <<SYS>>'''+self.system+'''<</SYS>>
                '''+self.instruction+'''
                [/INST]</s>'''
        )

    def generate_chat_prompt_template(self) -> ChatPromptTemplate:
        template = ChatPromptTemplate.from_messages([
            ("system", self.system),
            ("human", self.instruction)])
        return template

    def generate_simple_instruction(self, input_map) -> str:
        pt = self.generate_prompt_template(self)
        return pt.format(input_map)

class PromptTemplateRegistry:
    """A class that stores and tracks PromptTemplates for use within a given function."""

    # The name of this instruction template
    registry: Dict[str, PromptTemplateSpec] = {}

    def register_new_instruction_template(self, dict:Dict[str, str], override: bool = True):
        # check if all required fields are present
        assert 'name' in dict, "name is required"
        assert 'description' in dict, "description is required"
        assert 'system' in dict, "system is required"
        assert 'instruction' in dict, "instruction is required"
        assert 'input_variables' in dict, "input_variables is required"

        name = dict['name']
        description = dict['description']
        system = dict['system']
        instruction = dict['instruction']
        input_variables = dict['input_variables']
        output_variables = dict.get('output_variables')

        self.register_instruction_template( PromptTemplateSpec(name, description, system, instruction, input_variables), override=override)

    def deregister_instruction_template(self, name: str)->PromptTemplateSpec:
        instruction_template = self.registry.pop(name)
        return instruction_template

    def register_instruction_template(self, template: PromptTemplateSpec, override: bool = False):
        """Register a new conversation template."""
        if not override:
            assert template.name not in self.registry, f"{template.name} has been registered."
        self.registry[template.name] = template

    def get_prompt_template(self, name: str) -> PromptTemplateSpec:
        """Get a conversation template."""
        if name not in self.registry:
            raise ValueError(f"{name} has not been registered.")
        return self.registry[name]

    def load_prompts_from_yaml(self, file_name: str):
        prompts_yaml = files(prompts).joinpath(file_name).read_text()
        prompts_dict = yaml.safe_load(prompts_yaml)
        for pname in prompts_dict:
            dct = prompts_dict[pname]
            dct['name'] = pname
            self.register_new_instruction_template(dct)

    def __str__(self) -> str:
        out = "Registered instruction templates:\n"
        for name in self.registry:
            out += '- %s'%(name) + '\n'
        return out

# A global registry for all instruction templates
#global instructions
#instructions = PromptTemplateRegistry()
#instructions.load_prompts_from_yaml('tiab_prompts.yaml')

# %% ../nbs/00_core.ipynb 5
def load_alhazen_tool_environment():
    """Set broad variables for Alhazen.
    Currently only set default local file path."""
    if os.environ.get('LOCAL_FILE_PATH') is None: 
        raise Exception('Where are you storing your local literature database?')
    loc = os.environ['LOCAL_FILE_PATH']
    if loc[-1:] != '/':
        loc += '/'

    return loc

# %% ../nbs/00_core.ipynb 6
def lookup_chat_models() -> Dict[str, Any]:
    """Utility function to provide access to all available chat models."""

    llm_ollama_mixtral = ChatOllama(model='mixtral:instruct') 
    
    llm_gpt4_1106 = ChatOpenAI(model='gpt-4-1106-preview') 
    llm_gpt35 = ChatOpenAI(model='gpt-4-1106-preview') 
    llm_gemini10 = ChatVertexAI(model_name="gemini-1.0-pro", convert_system_message_to_human=True)
    
    chat_models = {        
        "ollama_mixtral": llm_ollama_mixtral,
        "gpt4.0": llm_gpt4_1106,
        'gpt3.5': llm_gpt35,
        'gemini1.0': llm_gemini10,
    }

    if os.environ.get('DB_API_KEY') is not None:
        llm_databricks_dbrx = ChatOpenAI(base_url='https://czi-shared-infra-czi-sci-general-prod-databricks.cloud.databricks.com/serving-endpoints', 
                        api_key=os.environ['DB_API_KEY'], 
                        model='databricks-dbrx-instruct')
        chat_models['databricks_dbrx'] = llm_databricks_dbrx
        llm_databricks_mixtral = ChatOpenAI(base_url='https://czi-shared-infra-czi-sci-general-prod-databricks.cloud.databricks.com/serving-endpoints', 
                        api_key=os.environ['DB_API_KEY'], 
                        model='databricks-mixtral-8x7b-instruct')
        chat_models['databricks_mixtral'] = llm_databricks_mixtral
        
    else:
        print('llm_databricks_* chat models are not available. Please set DB_API_KEY environment variable.')

    return chat_models

def lookup_embeddings() -> Dict[str, Any]:
    """Utility function to provide access to all available embedding models."""

    model_name = "BAAI/bge-large-en"
    if torch.backends.mps.is_available():
        model_kwargs = {"device": "mps"}
    elif torch.cuda.is_available():
        model_kwargs = {"device": "cuda"}
    else:
        model_kwargs = {"device": "cpu"}
    encode_kwargs = {"normalize_embeddings": True}
    hf_bge = HuggingFaceBgeEmbeddings(
      model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
    )
    embeddings = {        
        "hf_bge": hf_bge
    }

    return embeddings

# %% ../nbs/00_core.ipynb 7
class suppress_stdout_stderr(object):
    def __enter__(self):
        self.outnull_file = open(os.devnull, 'w')
        self.errnull_file = open(os.devnull, 'w')

        self.old_stdout_fileno_undup    = sys.stdout.fileno()
        self.old_stderr_fileno_undup    = sys.stderr.fileno()

        self.old_stdout_fileno = os.dup ( sys.stdout.fileno() )
        self.old_stderr_fileno = os.dup ( sys.stderr.fileno() )

        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

        os.dup2 ( self.outnull_file.fileno(), self.old_stdout_fileno_undup )
        os.dup2 ( self.errnull_file.fileno(), self.old_stderr_fileno_undup )

        sys.stdout = self.outnull_file        
        sys.stderr = self.errnull_file
        return self

    def __exit__(self, *_):        
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

        os.dup2 ( self.old_stdout_fileno, self.old_stdout_fileno_undup )
        os.dup2 ( self.old_stderr_fileno, self.old_stderr_fileno_undup )

        os.close ( self.old_stdout_fileno )
        os.close ( self.old_stderr_fileno )

        self.outnull_file.close()
        self.errnull_file.close()

# %% ../nbs/00_core.ipynb 8
class OllamaRunner:
    '''Class to run Ollama in a subprocess and to  
     run LLMs or chains locally with a timeout to 
     prevent long-running processes from hanging 
     the server.'''
    proc = None
        
    def __init__(self, model):
        self.llm = Ollama(model=model)

    async def _start_server(self):
        if self.proc is not None:
            self._terminate_server()
        self.proc = await asyncio.create_subprocess_shell(
            'ollama serve',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

    def _terminate_server(self):
        self.proc.terminate()
        self.proc = None

    def _callback(self, fut: asyncio.Future):
        if fut.cancelled() or not fut.done():
            print("Timed out! - Terminating server")
            fut.cancel()
            
    async def run_llm(self, prompt, timeout=300):
        # if server is not running, start it
        if self.proc is None:
            await self._start_server()
        # create task
        task = asyncio.create_task(self.llm.agenerate([prompt]))
        task.add_done_callback(self._callback)
        # try to await the task
        try:
            r = await asyncio.wait_for(task, timeout=timeout)
        except asyncio.TimeoutError as ex:
            print(ex)
        if r is not None:
            return '\n'.join([t[0].text for t in r.generations])
        else:
            return ''
        
    async def run_chain(self, chain, input, timeout=300):
        '''Incorporate the llm into a chain and run it.'''
        # if server is not running, start it
        if self.proc is None:
            await self._start_server()
        # create task
        task = asyncio.create_task(chain.ainvoke(input))
        task.add_done_callback(self._callback)
        # try to await the task
        try:
            r = await asyncio.wait_for(task, timeout=timeout)
        except asyncio.TimeoutError as ex:
            print(ex)
        return r
