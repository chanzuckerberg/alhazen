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
    from datetime import datetime

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
        datetime,
        desc,
        exists,
        func,
        functools,
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
        collection_counts = mo.ui.table(df2, selection='multi')
        mo.output.replace(collection_counts)
    except:
        print("Database not instantiated")
    return collection_counts, df2


@app.cell
def __(c_ids):
    collections_clause = ' OR '.join(['skc.id=\'{}\''.format(coll_id) for coll_id in c_ids])

    # Queries for each subtype of embedding
    q2_all = """
    SELECT DISTINCT skc.name, ske.id, ske.content, ske.publication_date as pub_date, ske.type as pub_type, emb.embedding, skf.content 
    FROM langchain_pg_embedding as emb, 
        "ScientificKnowledgeExpression" as ske,
        "ScientificKnowledgeCollection_has_members" as skc_hm, 
        "ScientificKnowledgeCollection" as skc, 
        "ScientificKnowledgeFragment" as skf
    WHERE emb.cmetadata->>'i_type' = 'CitationRecord' AND
        emb.cmetadata->>'e_id' = ske.id AND 
        emb.cmetadata->>'f_id' = skf.id AND
        skc_hm."ScientificKnowledgeCollection_id" = skc.id AND
        ske.id = skc_hm.has_members_id AND ({})
    ORDER BY pub_date DESC;
    """.format(collections_clause)

    q2_notes = """
    SELECT DISTINCT skc.name, ske.id, ske.content, ske.publication_date as pub_date, ske.type as pub_type, emb.embedding, skf.content 
    FROM langchain_pg_embedding as emb, 
        "ScientificKnowledgeExpression" as ske,
        "ScientificKnowledgeCollection_has_members" as skc_hm, 
        "ScientificKnowledgeCollection" as skc, 
        "ScientificKnowledgeFragment" as skf,
        "Note" as n,
        "Note_is_about" as nia
    WHERE n.type = 'MetadataExtractionNote' AND
        n.id = nia."Note_id" AND
        nia.is_about_id = ske.id AND
        emb.cmetadata->>'i_type' = 'CitationRecord' AND
        emb.cmetadata->>'e_id' = ske.id AND 
        emb.cmetadata->>'f_id' = skf.id AND
        skc_hm."ScientificKnowledgeCollection_id" = skc.id AND
        ske.id = skc_hm.has_members_id AND ({})
    ORDER BY pub_date DESC;
    """.format(collections_clause)
    return collections_clause, q2_all, q2_notes


@app.cell
def __(mo, q2_all, q2_notes, set_prunelist):
    map_type_dropdown = mo.ui.dropdown(
        options={"All papers": ('All', q2_all), 
                 "Papers with Metadata": ('Background', q2_notes)},
        value="All papers",
        label='Map type: '
    )
    paper_type_table = mo.ui.multiselect(
        options = {'Research Article': 'ScientificPrimaryResearchArticle',
                   'Research Preprint': 'ScientificPrimaryResearchPreprint',
                   'Review Article': 'ScientificReviewArticle', 
                   'Errata': 'ScientificErrata', 
                   'Comment': 'ScientificComment',
                   'Clinical Trial': 'ClinicalTrial'
                   },
        value= ['Research Article', 'Research Preprint'],
        label='Paper sub-type: ')
    set_prunelist([])
    mo.vstack([map_type_dropdown, paper_type_table,])
    return map_type_dropdown, paper_type_table


@app.cell
def __(embedding_df, mo, selected_dois, set_prunelist):
    prune_pb = mo.ui.button(label='Prune', value=selected_dois, on_click=set_prunelist)
    select_pb = mo.ui.button(label='Select', 
                             on_click=set_prunelist, 
                             value=[row.DOI for i, row in embedding_df.iterrows() if row.DOI not in selected_dois])
    clear_pb = mo.ui.button(label='Reset', on_click=set_prunelist, value=[])
    spr_buttons = mo.hstack([select_pb, prune_pb, clear_pb], justify="center")
    mo.left(spr_buttons)
    return clear_pb, prune_pb, select_pb, spr_buttons


@app.cell
def __(alt, embedding_df, mo):
    chart = mo.ui.altair_chart(
        alt.Chart(embedding_df)
        .mark_circle(size=10)
        .encode(
            x=alt.X("x:Q"),
            y=alt.Y("y:Q"),
            tooltip=["date", "Reference", "text"],
            color="Collection",
        )
        .properties(height=500),
        chart_selection="interval"
    )
    chart
    return chart,


@app.cell
def __(collection_counts):
    c_ids = collection_counts.value.reset_index()['id'].to_list()
    c_id = -1
    if len(collection_counts.value) > 0:
        c_id = collection_counts.value.reset_index().iloc[0]['id']
    return c_id, c_ids


@app.cell
def __(
    collection_counts,
    compute_embedding,
    get_prunelist,
    json,
    ldb,
    map_type_dropdown,
    mo,
    paper_type_table,
    pd,
    pymde,
    re,
    text,
    torch,
):
    mo.stop(collection_counts == None)
    map_type = map_type_dropdown.value[0]
    map_type_query = map_type_dropdown.value[1]
    ldb.session.rollback()
    rag_data = ldb.session.execute(text(map_type_query)).fetchall()

    rag_coll_list = []
    rag_id_list = []
    rag_ref_list = []
    rag_date_list = []
    rag_type_list = []
    rag_text_list = []
    rag_embeddings_list = []
    for cid, eid, ref, date, ptype, embed, txt in rag_data: 
        if eid in get_prunelist():
            #print(eid)
            continue
        if (ptype in paper_type_table.value) is False:
            #print(ptype)
            continue
        doi = re.sub('doi:', '', eid)
        doi_html = mo.Html('<a href="https://doi.org/'+doi+'">'+doi+'</a>')
        rag_coll_list.append(cid)
        rag_id_list.append(eid)
        rag_ref_list.append(ref)
        rag_date_list.append(date)
        rag_type_list.append(ptype)
        rag_embeddings_list.append(json.loads(embed))
        rag_text_list.append(txt)

    print(len(rag_embeddings_list))
    rag_embeddings_tensor = torch.FloatTensor(rag_embeddings_list)

    embedding_dimension = 2
    constraint = pymde.Standardized()
    embedding = compute_embedding(rag_embeddings_tensor, embedding_dimension, constraint)

    embedding_sampled = embedding.cpu()
    embedding_df = pd.DataFrame(
        {
            'Collection': rag_coll_list,
            'DOI': rag_id_list,
            'date': rag_date_list,
            'Reference': rag_ref_list,
            'Type': rag_type_list,
            "x": embedding_sampled[:, 0],
            "y": embedding_sampled[:, 1],
            'text': rag_text_list,
        }
    )
    embedding_df["date"] = pd.to_datetime(embedding_df["date"])
    return (
        cid,
        constraint,
        date,
        doi,
        doi_html,
        eid,
        embed,
        embedding,
        embedding_df,
        embedding_dimension,
        embedding_sampled,
        map_type,
        map_type_query,
        ptype,
        rag_coll_list,
        rag_data,
        rag_date_list,
        rag_embeddings_list,
        rag_embeddings_tensor,
        rag_id_list,
        rag_ref_list,
        rag_text_list,
        rag_type_list,
        ref,
        txt,
    )


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
def __(alt, papers_df, pd, resample_dropdown):
    def to_altair_datetime(dt):
        dt = pd.to_datetime(dt)
        return alt.DateTime(year=dt.year, month=dt.month, date=dt.day,
                            hours=dt.hour, minutes=dt.minute, seconds=dt.second,
                            milliseconds=0.001 * dt.microsecond)
    time_domain = [to_altair_datetime('2010-01-01'),
              to_altair_datetime('2024-06-01')]

    ts_df = papers_df.set_index('date') \
            .resample(resample_dropdown.value) \
            .count() \
            .reset_index(drop=False) \
            .drop(columns=['Reference', 'Type']) \
            .rename(columns={'DOI': 'Monthly Publication Count'})
    chart3 = alt.Chart(ts_df, width="container").mark_point().encode(
        x=alt.X('date:T'),#.scale(domain=time_domain),
        y='Monthly Publication Count'
    )
    chart3 + chart3.transform_loess('date', 'Monthly Publication Count').mark_line()
    return chart3, time_domain, to_altair_datetime, ts_df


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
def __(chart, collection_counts, embedding_df, ldb, mo):
    mo.stop(collection_counts == None)
    ldb.session.rollback()
    if len(chart.value) > 0:
        papers_df = chart.value.drop(columns=["x", "y", "text"])
    else:
        papers_df = embedding_df.drop(columns=["x", "y", "text"])
    papers_table = mo.ui.table(papers_df, selection='single')
    mo.as_html(papers_table)
    return papers_df, papers_table


@app.cell
def __(collection_counts, mo, papers_df):
    mo.stop(collection_counts == None)
    selected_dois = [row.DOI for i, row in papers_df.iterrows()]
    return selected_dois,


@app.cell
def __(collection_counts, mo):
    mo.stop(collection_counts == None)
    get_prunelist, set_prunelist = mo.state([])
    return get_prunelist, set_prunelist


if __name__ == "__main__":
    app.run()
