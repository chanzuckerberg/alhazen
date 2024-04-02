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
        distinct,
        exists,
        func,
        get_langchain_chatmodel,
        json,
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
def __(create_engine, mo, text):
    engine = create_engine('postgresql+psycopg2:///postgres')
    connection = engine.connect()
    result = connection.execute(text("SELECT datname FROM pg_database;"))
    dbn = [row[0] for row in result if row[0] != 'postgres']
    connection.close()

    ah_dbs = []
    for db in dbn:
        engine = create_engine('postgresql+psycopg2:///'+db)
        try: 
            connection = engine.connect()
            result = connection.execute(text('SELECT * FROM "ScientificKnowledgeCollection" LIMIT 1;'))
        except Exception as e:
            continue
        connection.close()    
        ah_dbs.append(db)

    if len(ah_dbs)>0:
        dropdown = mo.ui.dropdown(
            options={n:n for n in ah_dbs},
            value=ah_dbs[0],
            label='Available Databases: '
        )
        mo.output.replace(dropdown)
    return ah_dbs, connection, db, dbn, dropdown, engine, result


@app.cell
def _(dropdown, os):
    os.environ['ALHAZEN_DB_NAME'] = dropdown.value
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
    try:
        q = ldb.session.query(SKC.id, SKC.name, SKE.id, SKI.type) \
                .filter(SKC.id==SKC_HM.ScientificKnowledgeCollection_id) \
                .filter(SKC_HM.has_members_id==SKE.id) \
                .filter(SKE.id==SKE_HR.ScientificKnowledgeExpression_id) \
                .filter(SKE_HR.has_representation_id==SKI.id) 
        df1 = pd.DataFrame(q.all(), columns=['ID', 'collection', 'doi', 'type'])
        #ids = []
        #for i, row in df1.iterrows():
        #    try: 
        #        ids.append(row.ID.zfill(5))
        #    except: 
        #        ids.append(row.ID)
        #df1['ID'] = ids
        df2 = df1.pivot_table(index=['ID', 'collection'], 
                          columns='type', values='doi', 
                          aggfunc=lambda x: len(x.unique()))
        collection_counts = mo.ui.table(df2, selection='single')
        mo.output.replace(collection_counts)
    except:
        print("Database not instantiated")
    return collection_counts, df1, df2, q


@app.cell
def __(mo):
    doi_filter = mo.ui.text(label='Filter for DOI')
    return doi_filter,


@app.cell
def __(mo):
    citation_filter = mo.ui.text(label='Filter for Citation')
    return citation_filter,


@app.cell
def __(mo):
    extraction_complete = mo.ui.checkbox(label='Metadata Extraction Complete')
    return extraction_complete,


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
        papers_table = None
        if len(collection_counts.value) > 0:
            c_id = collection_counts.value.reset_index().iloc[0]['ID']
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
                            .filter(N.type == 'MetadataExtractionNote__cryoet') \
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
                            .filter(N.type == 'MetadataExtractionNote__cryoet') \
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
                            .filter(N.type == 'MetadataExtractionNote__cryoet') \
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
                            .filter(N.type == 'MetadataExtractionNote__cryoet') \
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
            papers_table = mo.ui.table(papers_df, selection='single')
            components = mo.vstack([doi_filter, citation_filter, extraction_complete, papers_table])
            mo.output.replace(components)
    return c_id, components, papers_df, papers_table, q2


@app.cell
def __(N, NIA, json, ldb, mo, papers_table, pd):

    p_id = -1
    report_df = None
    if papers_table is not None and len(papers_table.value) > 0:
        p_id = papers_table.value.iloc[0]['DOI']
        l = []
        q3 = ldb.session.query(N) \
            .filter(N.id == NIA.Note_id) \
            .filter(NIA.is_about_id == p_id) \
            .filter(N.type == 'MetadataExtractionNote__cryoet') 
        for n in q3.all():
            tup = json.loads(n.content)
            tup.pop('question')
            run_desc = json.loads(n.name)
            tup['variable'] = run_desc.get('variable')
            tup['run'] = n.creation_date
            l.append(tup)

        report_df = pd.DataFrame(l)
        if len(report_df)>0:
            #report_df = report_df[['variable', 'answer', 'gold_standard', 'run']]
            #report_table = mo.ui.table(report_df)
            
            with pd.option_context('display.max_rows', None,):
                mo.output.replace(report_df)
    return l, n, p_id, q3, report_df, run_desc, tup


if __name__ == "__main__":
    app.run()
