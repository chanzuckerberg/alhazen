# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['GGUF_LOOKUP_URL', 'MODEL_TYPE', 'PromptTemplateSpec', 'PromptTemplateRegistry', 'load_alhazen_tool_environment',
           'get_cached_gguf', 'get_langchain_embeddings', 'get_langchain_llm', 'get_langchain_chatmodel',
           'suppress_stdout_stderr', 'OllamaRunner']

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
from langchain_community.chat_models.openai import ChatOpenAI
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_community.llms.openai import OpenAI
from langchain_community.llms.ollama import Ollama 
from langchain.prompts import ChatPromptTemplate, PromptTemplate

import local_resources.prompts as prompts

import os
import signal
import subprocess
from time import sleep
from typing import List, Tuple, Any, Dict
import yaml 

# %% ../nbs/00_core.ipynb 4
# LIBRARY-WIDE CONSTANTS AND ENUMS 

GGUF_LOOKUP_URL = {
    "llama-2-70b-chat": "https://huggingface.co/TheBloke/Llama-2-70B-chat-GGUF/resolve/main/llama-2-70b-chat.Q5_K_M.gguf",
    "llama-2-13b-chat": "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q5_K_M.gguf",
    "llama-2-7b-chat": "https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf",
    "mistral-7b-instruct": "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf"
}

class MODEL_TYPE(Enum):
    Ollama = auto()
    LlamaCpp = auto()
    OpenAI = auto()


# %% ../nbs/00_core.ipynb 5
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

# %% ../nbs/00_core.ipynb 6
def load_alhazen_tool_environment():

    if os.environ.get('ALHAZEN_DB_NAME') is None: 
        raise Exception('Which database do you want to use for this application?')
    db_name = os.environ['ALHAZEN_DB_NAME']

    if os.environ.get('LOCAL_FILE_PATH') is None: 
        raise Exception('Where are you storing your local literature database?')
    loc = os.environ['LOCAL_FILE_PATH']
    if loc[-1:] != '/':
        loc += '/'
    
    return loc, db_name


# download GGUF files from HuggingFace URL and save it to disk in defined directory, return local file path
def get_cached_gguf(gguf_file: str) -> str:
    import requests
    import os
    from tqdm import tqdm
    from pathlib import Path

    if gguf_file not in GGUF_LOOKUP_URL:
        raise ValueError(f"{gguf_file} has not been registered.")
    
    url = GGUF_LOOKUP_URL[gguf_file]
    local_dir = os.environ['LLMS_TEMP_DIR']

    # create local directory if not exists
    Path(local_dir).mkdir(parents=True, exist_ok=True)

    # download file
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join(local_dir, local_filename)
    if not os.path.exists(local_filepath):
        r = requests.get(url, stream=True)
        with open(local_filepath, 'wb') as f:
            file_size = int(r.headers['content-length'])
            chunk_size = 1000
            with tqdm(ncols=100, desc="Downloading", total=file_size, unit_scale=True) as pbar:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
                    pbar.update(chunk_size)
    
    return local_filepath

def get_langchain_embeddings(model_type, **kwargs):

    if model_type == MODEL_TYPE.LlamaCpp or model_type == MODEL_TYPE.Ollama:
        model_name = "BAAI/bge-large-en"
        model_kwargs = {"device": "mps"}
        encode_kwargs = {"normalize_embeddings": True}
        llme = HuggingFaceBgeEmbeddings(
            model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
        )
        return llme
    
    elif model_type == MODEL_TYPE.OpenAI:    
        if os.environ.get('OPENAI_API_KEY') is None:
            raise ValueError(f"OPENAI_API_KEY env. variable not set.")

        openai_api_key = os.environ['OPENAI_API_KEY']
        llme = OpenAIEmbeddings(openai_api_key=openai_api_key)
        
        return llme

    else:
        raise ValueError(f"Unknown model {model_type}")

def get_langchain_llm(model_type, llm_name, **kwargs):

    if model_type == MODEL_TYPE.Ollama:

        return Ollama(model=llm_name)        

    elif model_type == MODEL_TYPE.LlamaCpp:

        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        n_gpu_layers = kwargs.get('n_gpu_layers', 1)
        temperature = kwargs.get('temperature', 0.1)
        n_batch = kwargs.get('n_batch', 512)  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
        model_path = get_cached_gguf(llm_name)
        n_ctx = kwargs.get('n_ctx', 4096)

        llm = LlamaCpp(
            model_path=model_path,
            n_ctx=n_ctx,
            n_gpu_layers=n_gpu_layers,
            temperature=temperature,
            n_batch=n_batch,
            callback_manager=callback_manager,
            f16_kv=True,
            verbose=True, # Verbose is required to pass to the callback manager
        )        

        return llm

    elif model_type == MODEL_TYPE.OpenAI:
        
        if os.environ.get('OPENAI_API_KEY') is None:
            raise ValueError(f"OPENAI_API_KEY env. variable not set.")

        openai_api_key = os.environ['OPENAI_API_KEY']
        llm = OpenAI(openai_api_key=openai_api_key, model_name=llm_name)
        
        return llm 


def get_langchain_chatmodel(model_type, llm_name, **kwargs):

    if model_type == MODEL_TYPE.Ollama:

        return ChatOllama(model=llm_name)        

    elif model_type == MODEL_TYPE.LlamaCpp:

        raise Exception("Can't run Chat Models with LLamaCPP")

    elif model_type == MODEL_TYPE.OpenAI:
        
        if os.environ.get('OPENAI_API_KEY') is None:
            raise ValueError(f"OPENAI_API_KEY env. variable not set.")

        openai_api_key = os.environ['OPENAI_API_KEY']
        llm = ChatOpenAI(openai_api_key=openai_api_key, model_name=llm_name)
        
        return llm 

    else:

        raise ValueError(f"Unknown model {model_type}")
    

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
