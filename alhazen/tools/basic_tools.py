# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/10_basic_tools.ipynb.

# %% auto 0
__all__ = ['SearchSchema', 'CustomSearchTool']

# %% ../../nbs/10_basic_tools.ipynb 4
from typing import Optional, Type

from langchain.tools import StructuredTool
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.agents import AgentType, initialize_agent
from langchain.chains import LLMMathChain
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.utilities import SerpAPIWrapper
from langchain.pydantic_v1 import BaseModel, Field


# %% ../../nbs/10_basic_tools.ipynb 5
class SearchSchema(BaseModel):
    query: str = Field(description="should be a search query")
    engine: str = Field(description="should be a search engine")
    gl: str = Field(description="should be a country code")
    hl: str = Field(description="should be a language code")

class CustomSearchTool(BaseTool):
    name = "custom_search"
    description = "useful for when you need to answer questions about current events"

    def _run(
        self,
        query: str,
        engine: str = "google",
        gl: str = "us",
        hl: str = "en",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        search_wrapper = SerpAPIWrapper(params={"engine": engine, "gl": gl, "hl": hl})
        return search_wrapper.run(query)

    async def _arun(
        self,
        query: str,
        engine: str = "google",
        gl: str = "us",
        hl: str = "en",
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")

class CustomSearchTool(BaseTool):
    name = "custom_search"
    description = "useful for when you need to answer questions about current events"
    args_schema: Type[SearchSchema] = SearchSchema

    def _run(
        self,
        query: str,
        engine: str = "google",
        gl: str = "us",
        hl: str = "en",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        search_wrapper = SerpAPIWrapper(params={"engine": engine, "gl": gl, "hl": hl})
        return search_wrapper.run(query)

    async def _arun(
        self,
        query: str,
        engine: str = "google",
        gl: str = "us",
        hl: str = "en",
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")
