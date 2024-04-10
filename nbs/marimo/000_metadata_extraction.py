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
        # Alhazen Metadata Extraction Dashboard  

        > Tables of extracted metadatafrom papers across all local Alhazen databases.
        """
    )
    return


@app.cell
def _():
    from alhazen.aliases import IR, N, NIA, SKC, SKC_HM, SKC_HN, SKE, SKE_HN, SKE_HR, \
            SKE_IRI, SKE_MO, SKE_XREF, SKF, SKF_HN, SKI, SKI_HN, SKI_HP

    from alhazen.core import get_langchain_chatmodel, MODEL_TYPE
    from alhazen.utils.ceifns_db import list_databases, Ceifns_LiteratureDb

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

    from sqlalchemy import create_engine, text, exists, func, or_, and_, not_, desc, asc, distinct
    from sqlalchemy.orm import sessionmaker, aliased

    from time import time,sleep
    from tqdm import tqdm
    from urllib.request import urlopen
    from urllib.parse import quote_plus, quote, unquote
    from urllib.error import URLError, HTTPError
    import yaml
    return (
        Ceifns_LiteratureDb,
        CharacterTextSplitter,
        ChatOllama,
        ChatOpenAI,
        ChatVertexAI,
        ConsoleCallbackHandler,
        Document,
        HTTPError,
        IR,
        MODEL_TYPE,
        N,
        NIA,
        PGVector,
        Path,
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
        URLError,
        aliased,
        alt,
        and_,
        asc,
        create_engine,
        desc,
        distinct,
        exists,
        func,
        get_langchain_chatmodel,
        json,
        list_databases,
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
def __(list_databases, mo):
    ah_dbs = list_databases()
    if len(ah_dbs)>0:
        dropdown = mo.ui.dropdown(
            options={n:n for n in ah_dbs},
            value=ah_dbs[0],
            label='Available Databases: '
        )
        mo.output.replace(dropdown)
    return ah_dbs, dropdown


@app.cell
def __(Ceifns_LiteratureDb, dropdown, os):
    db_name = dropdown.value
    loc = os.environ['LOCAL_FILE_PATH']
    ldb = Ceifns_LiteratureDb(loc=loc, name=db_name)
    return db_name, ldb, loc


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Scientific Knowledge Collections
        """
    )
    return


@app.cell
def _(ldb, mo):
    try:
        df2 = ldb.report_collection_composition()
        collection_counts = mo.ui.table(df2, selection='single')
        mo.output.replace(collection_counts)
    except:
        print("Database not instantiated")
    return collection_counts, df2


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Papers
        """
    )
    return


@app.cell
def __(mo):
    doi_filter = mo.ui.text(label='Filter for DOI')
    citation_filter = mo.ui.text(label='Filter for Citation')
    extraction_complete = mo.ui.checkbox(label='Metadata Extraction Complete')

    return citation_filter, doi_filter, extraction_complete


@app.cell
def __(
    N,
    NIA,
    SKC,
    SKC_HM,
    SKE,
    citation_filter,
    collection_counts,
    doi_filter,
    extraction_complete,
    ldb,
    mo,
    or_,
    pd,
):
    papers_table = None
    if collection_counts:
        c_id = -1
        if len(collection_counts.value) > 0:
            c_id = collection_counts.value.reset_index().iloc[0]['id']
            if extraction_complete.value:
                if doi_filter.value and citation_filter.value is None:
                    q2 = ldb.session.query(SKE.id, SKE.content) \
                            .distinct() \
                            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                            .filter(SKC_HM.has_members_id==SKE.id) \
                            .filter(or_(SKE.type=='ScientificPrimaryResearchArticle', \
                                        SKE.type=='ScientificPrimaryResearchPreprint')) \
                            .filter(SKC.id==c_id) \
                            .filter(NIA.is_about_id == SKE.id) \
                            .filter(N.id == NIA.Note_id) \
                            .filter(N.type == 'MetadataExtractionNote') \
                            .filter(SKE.id.like('%'+doi_filter.value+'%'))
                elif doi_filter.value is None and citation_filter.value is None: 
                    q2 = ldb.session.query(SKE.id, SKE.content) \
                            .distinct() \
                            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                            .filter(SKC_HM.has_members_id==SKE.id) \
                            .filter(or_(SKE.type=='ScientificPrimaryResearchArticle', \
                                        SKE.type=='ScientificPrimaryResearchPreprint')) \
                            .filter(NIA.is_about_id == SKE.id) \
                            .filter(N.id == NIA.Note_id) \
                            .filter(N.type == 'MetadataExtractionNote') \
                            .filter(SKC.id==c_id)
                elif doi_filter.value is None and citation_filter.value: 
                    q2 = ldb.session.query(SKE.id, SKE.content) \
                            .distinct() \
                            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                            .filter(SKC_HM.has_members_id==SKE.id) \
                            .filter(or_(SKE.type=='ScientificPrimaryResearchArticle', \
                                        SKE.type=='ScientificPrimaryResearchPreprint')) \
                            .filter(NIA.is_about_id == SKE.id) \
                            .filter(N.id == NIA.Note_id) \
                            .filter(N.type == 'MetadataExtractionNote') \
                            .filter(SKC.id==c_id) \
                            .filter(SKE.content.like('%'+citation_filter.value+'%'))
                else: 
                    q2 = ldb.session.query(SKE.id, SKE.content) \
                            .distinct() \
                            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                            .filter(SKC_HM.has_members_id==SKE.id) \
                            .filter(or_(SKE.type=='ScientificPrimaryResearchArticle', \
                                        SKE.type=='ScientificPrimaryResearchPreprint')) \
                            .filter(NIA.is_about_id == SKE.id) \
                            .filter(N.id == NIA.Note_id) \
                            .filter(N.type == 'MetadataExtractionNote') \
                            .filter(SKC.id==c_id) \
                            .filter(SKE.id.like('%'+doi_filter.value+'%')) \
                            .filter(SKE.content.like('%'+citation_filter.value+'%'))
            else:
                if doi_filter.value and citation_filter.value is None:
                    q2 = ldb.session.query(SKE.id, SKE.content) \
                            .distinct() \
                            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                            .filter(SKC_HM.has_members_id==SKE.id) \
                            .filter(or_(SKE.type=='ScientificPrimaryResearchArticle', \
                                        SKE.type=='ScientificPrimaryResearchPreprint')) \
                            .filter(SKC.id==c_id) \
                            .filter(SKE.id.like('%'+doi_filter.value+'%'))
                elif doi_filter.value is None and citation_filter.value is None: 
                    q2 = ldb.session.query(SKE.id, SKE.content) \
                            .distinct() \
                            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                            .filter(SKC_HM.has_members_id==SKE.id) \
                            .filter(or_(SKE.type=='ScientificPrimaryResearchArticle', \
                                        SKE.type=='ScientificPrimaryResearchPreprint')) \
                            .filter(SKC.id==c_id)
                elif doi_filter.value is None and citation_filter.value: 
                    q2 = ldb.session.query(SKE.id, SKE.content) \
                            .distinct() \
                            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                            .filter(SKC_HM.has_members_id==SKE.id) \
                            .filter(or_(SKE.type=='ScientificPrimaryResearchArticle', \
                                        SKE.type=='ScientificPrimaryResearchPreprint')) \
                            .filter(SKC.id==c_id) \
                            .filter(SKE.content.like('%'+citation_filter.value+'%'))
                else: 
                    q2 = ldb.session.query(SKE.id, SKE.content) \
                            .distinct() \
                            .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                            .filter(SKC_HM.has_members_id==SKE.id) \
                            .filter(or_(SKE.type=='ScientificPrimaryResearchArticle', \
                                        SKE.type=='ScientificPrimaryResearchPreprint')) \
                            .filter(SKC.id==c_id) \
                            .filter(SKE.id.like('%'+doi_filter.value+'%')) \
                            .filter(SKE.content.like('%'+citation_filter.value+'%'))

            papers_df = pd.DataFrame(q2.all(), columns=['DOI', 'Reference'])
            papers_table = mo.ui.table(papers_df, selection='multi')
            components = mo.vstack([doi_filter, citation_filter, extraction_complete, papers_table])
            mo.output.replace(components)
    return c_id, components, papers_df, papers_table, q2


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Metadata Extraction
        """
    )
    return


@app.cell
def __(N, NIA, json, ldb, mo, papers_table, pd):
    p_id = -1
    report_df = None
    if papers_table is not None and len(papers_table.value) > 0:
        l = []
        for i2,row2 in papers_table.value.iterrows():
            p_id = row2.DOI
            q3 = ldb.session.query(N) \
                .filter(N.id == NIA.Note_id) \
                .filter(NIA.is_about_id == p_id) \
                .filter(N.type == 'MetadataExtractionNote') 
            for n in q3.all():
                tup = json.loads(n.content)
                tup['DOI'] = p_id
                l.append(tup)

        report_df = pd.DataFrame(l).set_index('DOI')
        if len(report_df)>0:
            with pd.option_context('display.max_rows', None,):
                report_table = mo.ui.table(report_df, selection='multi')
                mo.output.replace(report_table)
    return i2, l, n, p_id, q3, report_df, report_table, row2, tup


if __name__ == "__main__":
    app.run()
