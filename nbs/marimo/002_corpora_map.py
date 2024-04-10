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
        # Alhazen Literature Dashboard  

        > Dashboard for literature collection exploration.
        """
    )
    return


@app.cell
def _():
    import functools

    import pymde
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

    from sqlalchemy import cast, Date, create_engine, text, exists, func, or_, and_, not_, desc, asc
    from sqlalchemy.orm import sessionmaker, aliased

    from time import time,sleep
    import torch

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
        Date,
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
        cast,
        create_engine,
        desc,
        exists,
        func,
        functools,
        get_langchain_chatmodel,
        json,
        list_databases,
        mo,
        not_,
        or_,
        os,
        pd,
        pymde,
        quote,
        quote_plus,
        re,
        requests,
        sessionmaker,
        sleep,
        text,
        time,
        torch,
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
def _(Ceifns_LiteratureDb, dropdown, os):
    db_name = dropdown.value
    loc = os.environ['LOCAL_FILE_PATH']
    ldb = Ceifns_LiteratureDb(loc=loc, name=db_name)
    return db_name, ldb, loc


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
def _(ldb, mo):
    try:
        df2 = ldb.report_collection_composition()
        collection_counts = mo.ui.table(df2, selection='single')
        mo.output.replace(collection_counts)
    except:
        print("Database not instantiated")
    return collection_counts, df2


@app.cell
def __(alt, embedding_df, mo):
    chart = mo.ui.altair_chart(
        alt.Chart(embedding_df)
        .mark_circle(size=5)
        .encode(
            x=alt.X("x:Q").scale(domain=(-2.5, 2.5)),
            y=alt.Y("y:Q").scale(domain=(-2.5, 2.5)),
        ).properties(width=500, height=500),
        chart_selection="interval"
    )
    chart
    return chart,


@app.cell
def __(collection_counts):
    c_id = -1
    if len(collection_counts.value) > 0:
        c_id = collection_counts.value.reset_index().iloc[0]['id']
    return c_id,


@app.cell
def __(c_id, collection_counts, json, ldb, mo, text, torch):
    mo.stop(collection_counts == None)
    query = """
    SELECT DISTINCT ske.id, ske.content, ske.publication_date as pub_date, ske.type as pub_type, emb.embedding 
    FROM langchain_pg_embedding as emb, 
        "ScientificKnowledgeExpression" as ske,
        "ScientificKnowledgeCollection_has_members" as skc_hm
    WHERE emb.cmetadata->>'i_type' = 'CitationRecord' AND
        emb.cmetadata->>'e_id' = ske.id AND 
        ske.id = skc_hm.has_members_id AND
        skc_hm."ScientificKnowledgeCollection_id"='{}'
    ORDER BY pub_date DESC;
    """.format(c_id)
    rag_data = ldb.session.execute(text(query)).fetchall()
    rag_id_list = [r[0] for r in rag_data]
    rag_ref_list = [r[1] for r in rag_data]
    rag_date_list = [r[2] for r in rag_data]
    rag_type_list = [r[3] for r in rag_data]
    rag_embeddings_list = [json.loads(r[4]) for r in rag_data]
    rag_embeddings_tensor = torch.FloatTensor(rag_embeddings_list)
    return (
        query,
        rag_data,
        rag_date_list,
        rag_embeddings_list,
        rag_embeddings_tensor,
        rag_id_list,
        rag_ref_list,
        rag_type_list,
    )


@app.cell
def __(
    collection_counts,
    compute_embedding,
    mo,
    pymde,
    rag_embeddings_tensor,
):
    mo.stop(collection_counts == None)
    embedding_dimension = 2
    constraint = pymde.Standardized()
    embedding = compute_embedding(rag_embeddings_tensor, embedding_dimension, constraint)
    return constraint, embedding, embedding_dimension


@app.cell
def __(
    collection_counts,
    embedding,
    mo,
    pd,
    rag_date_list,
    rag_id_list,
    rag_ref_list,
    rag_type_list,
):
    mo.stop(collection_counts == None)
    embedding_sampled = embedding.cpu()
    embedding_df = pd.DataFrame(
        {
            'DOI': rag_id_list,
            'date': rag_date_list,
            'Reference': rag_ref_list,
            'Type': rag_type_list,
            "x": embedding_sampled[:, 0],
            "y": embedding_sampled[:, 1],
        }
    )
    embedding_df["date"] = pd.to_datetime(embedding_df["date"])
    return embedding_df, embedding_sampled


@app.cell
def __(functools, mo, pymde):
    @functools.cache
    def compute_embedding(data, embedding_dim, constraint):
        mo.output.append(
            mo.md("Your embedding is being computed ... hang tight!").callout(kind="warn")
        )

        mde = pymde.preserve_neighbors(
            data,
            embedding_dim=embedding_dim,
            constraint=constraint,
            device="mps",
            verbose=True,
        )
        X = mde.embed(verbose=True)
        mo.output.clear()
        return X
    return compute_embedding,


@app.cell
def __(alt, papers_df, resample_dropdown):
    ts_df = papers_df.set_index('date') \
            .resample(resample_dropdown.value) \
            .count() \
            .reset_index(drop=False) \
            .drop(columns=['Reference', 'Type']) \
            .rename(columns={'DOI': 'Monthly Publication Count'})
    chart3 = alt.Chart(ts_df, width="container").mark_point().encode(
        x='date',
        y='Monthly Publication Count'
    )
    chart3 + chart3.transform_loess('date', 'Monthly Publication Count').mark_line()
    return chart3, ts_df


@app.cell
def __(mo):
    resample_dropdown = mo.ui.dropdown(
      options=['1M', '2M', '3M', '6M', '1Y'],
      value='3M',
      label='Sampling Interval'
    )
    resample_dropdown
    return resample_dropdown,


@app.cell
def __(chart, collection_counts, embedding_df, mo):
    mo.stop(collection_counts == None)
    papers_table = None

    if len(chart.value) > 0:
        papers_df = chart.value.drop(columns=['x','y'])
    else:
        papers_df = embedding_df.drop(columns=['x','y'])

    papers_table = mo.ui.table(papers_df, selection='multi')
    mo.output.replace(papers_table)
    return papers_df, papers_table


if __name__ == "__main__":
    app.run()
