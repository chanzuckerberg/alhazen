import marimo

__generated_with = "0.2.13"
app = marimo.App(
    width="full",
    layout_file="layouts/001a_CryoET_Metadata_Marimo.grid.json",
)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Alhazen Chat  

        > Simple chatbot interface to run commmands within Alhazen.
        """
    )
    return


@app.cell
def _():
    from alhazen.agent import AlhazenAgent
<<<<<<< HEAD
    from alhazen.core import lookup_chat_models
=======
>>>>>>> 75dc97aff9dc932799675920edfaed089bf106a3
    from alhazen.schema_sqla import InformationResource, \
            ScientificKnowledgeCollection, \
            ScientificKnowledgeCollectionHasMembers, \
            ScientificKnowledgeExpression, \
            ScientificKnowledgeExpressionXref, \
            ScientificKnowledgeExpressionIri, \
            ScientificKnowledgeExpressionHasRepresentation, \
            ScientificKnowledgeExpressionMemberOf, \
            ScientificKnowledgeItem, \
            ScientificKnowledgeItemHasPart, \
            ScientificKnowledgeFragment, \
            Note, NoteIsAbout, \
            ScientificKnowledgeCollectionHasNotes, \
            ScientificKnowledgeExpressionHasNotes, \
            ScientificKnowledgeItemHasNotes, \
            ScientificKnowledgeFragmentHasNotes
    from alhazen.utils.ceifns_db import Ceifns_LiteratureDb, list_databases

    import altair as alt
    import json

    from langchain.callbacks.tracers import ConsoleCallbackHandler
    from langchain.docstore.document import Document
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores.pgvector import PGVector
    from langchain_community.chat_models.ollama import ChatOllama
    from langchain_google_vertexai import ChatVertexAI
    from langchain_openai import ChatOpenAI

    import marimo as mo
    import os
    import pandas as pd
    from pathlib import Path
    import re
    import requests

    from sqlalchemy import create_engine, text, exists, func, or_, and_, not_, desc, asc
    from sqlalchemy.orm import sessionmaker, aliased

    from time import time,sleep
    from tqdm import tqdm
    from urllib.request import urlopen
    from urllib.parse import quote_plus, quote, unquote
    from urllib.error import URLError, HTTPError
    import yaml
    return (
        AlhazenAgent,
        Ceifns_LiteratureDb,
        CharacterTextSplitter,
        ChatOllama,
        ChatOpenAI,
        ChatVertexAI,
        ConsoleCallbackHandler,
        Document,
        HTTPError,
        InformationResource,
        Note,
        NoteIsAbout,
        PGVector,
        Path,
        ScientificKnowledgeCollection,
        ScientificKnowledgeCollectionHasMembers,
        ScientificKnowledgeCollectionHasNotes,
        ScientificKnowledgeExpression,
        ScientificKnowledgeExpressionHasNotes,
        ScientificKnowledgeExpressionHasRepresentation,
        ScientificKnowledgeExpressionIri,
        ScientificKnowledgeExpressionMemberOf,
        ScientificKnowledgeExpressionXref,
        ScientificKnowledgeFragment,
        ScientificKnowledgeFragmentHasNotes,
        ScientificKnowledgeItem,
        ScientificKnowledgeItemHasNotes,
        ScientificKnowledgeItemHasPart,
        URLError,
        aliased,
        alt,
        and_,
        asc,
        create_engine,
        desc,
        exists,
        func,
        json,
        list_databases,
<<<<<<< HEAD
        lookup_chat_models,
=======
>>>>>>> 75dc97aff9dc932799675920edfaed089bf106a3
        mo,
        not_,
        or_,
        os,
        pd,
        quote,
        quote_plus,
        re,
        requests,
        sessionmaker,
        sleep,
        text,
        time,
        tqdm,
        unquote,
        urlopen,
        yaml,
    )


@app.cell
def __(
    InformationResource,
    Note,
    NoteIsAbout,
    ScientificKnowledgeCollection,
    ScientificKnowledgeCollectionHasMembers,
    ScientificKnowledgeCollectionHasNotes,
    ScientificKnowledgeExpression,
    ScientificKnowledgeExpressionHasNotes,
    ScientificKnowledgeExpressionHasRepresentation,
    ScientificKnowledgeExpressionIri,
    ScientificKnowledgeExpressionMemberOf,
    ScientificKnowledgeExpressionXref,
    ScientificKnowledgeFragment,
    ScientificKnowledgeFragmentHasNotes,
    ScientificKnowledgeItem,
    ScientificKnowledgeItemHasNotes,
    ScientificKnowledgeItemHasPart,
    aliased,
):
    IR = aliased(InformationResource)

    SKC = aliased(ScientificKnowledgeCollection)
    SKC_HM = aliased(ScientificKnowledgeCollectionHasMembers)
    SKE = aliased(ScientificKnowledgeExpression)
    SKE_XREF = aliased(ScientificKnowledgeExpressionXref)
    SKE_IRI = aliased(ScientificKnowledgeExpressionIri)
    SKE_HR = aliased(ScientificKnowledgeExpressionHasRepresentation)
    SKE_MO = aliased(ScientificKnowledgeExpressionMemberOf)
    SKI = aliased(ScientificKnowledgeItem)
    SKI_HP = aliased(ScientificKnowledgeItemHasPart)
    SKF = aliased(ScientificKnowledgeFragment)

    N = aliased(Note)
    NIA = aliased(NoteIsAbout)
    SKC_HN = aliased(ScientificKnowledgeCollectionHasNotes)
    SKE_HN = aliased(ScientificKnowledgeExpressionHasNotes)
    SKI_HN = aliased(ScientificKnowledgeItemHasNotes)
    SKF_HN = aliased(ScientificKnowledgeFragmentHasNotes)
    return (
        IR,
        N,
        NIA,
        SKC,
        SKC_HM,
        SKC_HN,
        SKE,
        SKE_HN,
        SKE_HR,
        SKE_IRI,
        SKE_MO,
        SKE_XREF,
        SKF,
        SKF_HN,
        SKI,
        SKI_HN,
        SKI_HP,
    )


@app.cell
def __(list_databases, mo):
    dbn = list_databases()
    dropdown = mo.ui.dropdown(
        options={n:n for n in dbn},
        value=dbn[0],
        label='Available Databases: '
        )

    dropdown
    return dbn, dropdown


@app.cell
def _(dropdown, os):
<<<<<<< HEAD
    db_name = dropdown.value
=======
    os.environ['ALHAZEN_DB_NAME'] = dropdown.value
>>>>>>> 75dc97aff9dc932799675920edfaed089bf106a3

    if os.path.exists(os.environ['LOCAL_FILE_PATH']) is False:
        os.makedirs(os.environ['LOCAL_FILE_PATH'])

<<<<<<< HEAD
=======
    if os.environ.get('ALHAZEN_DB_NAME') is None: 
        raise Exception('Which database do you want to use for this application?')
    db_name = os.environ['ALHAZEN_DB_NAME']

>>>>>>> 75dc97aff9dc932799675920edfaed089bf106a3
    if os.environ.get('LOCAL_FILE_PATH') is None: 
        raise Exception('Where are you storing your local literature database?')
    loc = os.environ['LOCAL_FILE_PATH']
    return db_name, loc


@app.cell
def __(
    AlhazenAgent,
    Ceifns_LiteratureDb,
<<<<<<< HEAD
    db_name,
    loc,
    lookup_chat_models,
):
    ldb = Ceifns_LiteratureDb(loc=loc, name=db_name)
    llms_lookup = lookup_chat_models()
    llm = llms_lookup.get('databricks_llama3')

    de = AlhazenAgent(llm, llm, db_name=db_name)

    return de, ldb, llm, llms_lookup
=======
    ChatOllama,
    ChatOpenAI,
    db_name,
    loc,
):
    ldb = Ceifns_LiteratureDb(loc=loc, name=db_name)
    llm_mixtral = ChatOllama(model='mixtral:instruct') 
    llm_gpt35 = ChatOpenAI(model='gpt-3.5-turbo-0125') 
    llm_gpt4 = ChatOpenAI(model='gpt-4-1106-preview') 

    de = AlhazenAgent(llm_mixtral, llm_mixtral)
    return de, ldb, llm_gpt35, llm_gpt4, llm_mixtral
>>>>>>> 75dc97aff9dc932799675920edfaed089bf106a3


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Scientific Knowledge Collections

        Numbers of Scientific Knowledge Item (`SKI`) entities in Collections, broken down by item type (corresponding to the type of data available).
        """
    )
    return


@app.cell
def __(SKC, SKC_HM, SKE, SKE_HR, SKI, ldb, mo, pd):
    try:
        q = ldb.session.query(SKC.id, SKC.name, SKE.id, SKI.type) \
                .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                .filter(SKC_HM.has_members_id==SKE.id) \
                .filter(SKE.id==SKE_HR.ScientificKnowledgeExpression_id) \
                .filter(SKE_HR.has_representation_id==SKI.id) 
        df1 = pd.DataFrame(q.all(), columns=['ID', 'collection', 'doi', 'type'])
        ids = []
        for i, row in df1.iterrows():
            try: 
                ids.append(row.ID.zfill(5))
            except: 
                ids.append(row.ID)
        df1['ID'] = ids
        df2 = df1.pivot_table(index=['ID', 'collection'], 
                          columns='type', values='doi', 
                          aggfunc=lambda x: len(x.unique()))
        t = mo.ui.table(df2, selection='single')
        mo.output.replace(t)
    except:
        print("Database not instantiated")
    return df1, df2, i, ids, q, row, t


@app.cell
def __(de, e, mo):
    #~~~~~~~~~~~~~~~~~~~~~~
    # Update chat
    #~~~~~~~~~~~~~~~~~~~~~~

    def update_chat():
        msg_md_components = []
        for c in messages:
            if c[0] == 'system':
                m = mo.md('>**'+c[1]+'**').left() 
            elif c[0] == 'user':
                m = mo.md('>*'+c[1]+'*').right() 
            msg_md_components.append(m)
        msg_md_components.append(chat_command)
        msg_stack = mo.vstack(msg_md_components)
        mo.output.replace(msg_stack)

    def invoke_agent(value):
        if value is not None and len(value) > 0:
            chat_command.disabled = True
            messages.append(('user', value))
            update_chat()
            try:
                response = de.agent_executor.invoke({'input': value})
                if isinstance(response.get('output'), dict): 
                    if response.get('output').get('response'): 
                        r = response.get('output').get('response')
                    else:
                        r = str(response.get('output'))
                elif isinstance(response.get('output'), str): 
                    r = response.get('output')
                messages.append(('system', r))
            except Exception as e:
                messages.append(('system', f'Error: {e}'))
        else:
            print(value)
        update_chat()
        chat_command.disabled = True

    #~~~~~~~~~~~~~~
    # Chat command.
    #~~~~~~~~~~~~~~
    messages = []
    chat_command = mo.ui.text_area(
        placeholder='Enter command for Alhazen...', 
        rows=2,
        full_width=True, on_change=invoke_agent
    ).form(clear_on_submit=True,
           bordered=False)
    update_chat()
    return chat_command, invoke_agent, messages, update_chat


if __name__ == "__main__":
    app.run()
