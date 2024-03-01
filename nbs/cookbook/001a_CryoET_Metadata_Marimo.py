import marimo

__generated_with = "0.2.13"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(
        r"""
        # CryoET Literature Dashboard  

        > Data dashboards, visualizations and tools to explore the CryoET Literature.
        """
    )
    return


@app.cell
def _():
    from alhazen.apps.chat import  AlhazenAgentChatBot
    from alhazen.core import get_langchain_chatmodel, MODEL_TYPE
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
    from alhazen.utils.ceifns_db import Ceifns_LiteratureDb

    import altair as alt

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

    from sqlalchemy import create_engine, exists, func, or_, and_, not_, desc, asc
    from sqlalchemy.orm import sessionmaker, aliased

    from time import time,sleep
    from tqdm import tqdm
    from urllib.request import urlopen
    from urllib.parse import quote_plus, quote, unquote
    from urllib.error import URLError, HTTPError
    import yaml
    return (
        AlhazenAgentChatBot,
        Ceifns_LiteratureDb,
        CharacterTextSplitter,
        ChatOllama,
        ChatOpenAI,
        ChatVertexAI,
        ConsoleCallbackHandler,
        Document,
        HTTPError,
        InformationResource,
        MODEL_TYPE,
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
        get_langchain_chatmodel,
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
        time,
        tqdm,
        unquote,
        urlopen,
        yaml,
    )


@app.cell
def _(
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
    # Using Aliases like this massively simplifies the use of SQLAlchemy
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
def _(os):
    os.environ['ALHAZEN_DB_NAME'] = 'em_tech'
    os.environ['LOCAL_FILE_PATH'] = '/users/gully.burns/alhazen/'

    if os.path.exists(os.environ['LOCAL_FILE_PATH']) is False:
        os.makedirs(os.environ['LOCAL_FILE_PATH'])

    if os.environ.get('ALHAZEN_DB_NAME') is None: 
        raise Exception('Which database do you want to use for this application?')
    db_name = os.environ['ALHAZEN_DB_NAME']

    if os.environ.get('LOCAL_FILE_PATH') is None: 
        raise Exception('Where are you storing your local literature database?')
    loc = os.environ['LOCAL_FILE_PATH']
    return db_name, loc


@app.cell
def _(Ceifns_LiteratureDb, db_name, loc):
    ldb = Ceifns_LiteratureDb(loc=loc, name=db_name)
    return ldb,


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
def _(SKC, SKC_HM, SKE, SKE_HR, SKI, ldb, mo, pd):
    q = ldb.session.query(SKC.id, SKC.name, SKE.id, SKI.type) \
            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
            .filter(SKC_HM.has_members_id==SKE.id) \
            .filter(SKE.id==SKE_HR.ScientificKnowledgeExpression_id) \
            .filter(SKE_HR.has_representation_id==SKI.id) 
    df1 = pd.DataFrame(q.all(), columns=['ID', 'collection', 'doi', 'type'])    
    df2 = df1.pivot_table(index=['ID', 'collection'], 
                          columns='type', values='doi', 
                          aggfunc=lambda x: len(x.unique()))
    collection_counts = mo.ui.table(df2, selection='single')
    collection_counts
    return collection_counts, df1, df2, q


@app.cell
def __(collection_counts):
    collection_counts.value
    return


if __name__ == "__main__":
    app.run()
