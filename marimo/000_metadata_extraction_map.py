import marimo

<<<<<<< HEAD
__generated_with = "0.2.13"
=======
__generated_with = "0.6.23"
>>>>>>> 75dc97aff9dc932799675920edfaed089bf106a3
app = marimo.App(width="full")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Collection Dashboard  

        > Dashboard for literature collection exploration.
        """
    )
    return


@app.cell
def _():
    import functools

    from alhazen.aliases import IR, N, NIA, SKC, SKC_HM, SKC_HN, SKE, SKE_HN, SKE_HR, \
            SKE_IRI, SKE_MO, SKE_XREF, SKF, SKF_HN, SKI, SKI_HN, SKI_HP
    from alhazen.utils.ceifns_db import list_databases, Ceifns_LiteratureDb

    import json

    from langchain.callbacks.tracers import ConsoleCallbackHandler
    from langchain.docstore.document import Document
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores.pgvector import PGVector
    from langchain_community.chat_models.ollama import ChatOllama
    from langchain_google_vertexai import ChatVertexAI
    from langchain_openai import ChatOpenAI

    import altair as alt
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
    import pymde

    import nltk
    success = nltk.download('punkt')
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
        nltk,
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
        success,
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
    dropdown = None
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
    if dropdown:
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
        select_collection_form = mo.ui.form(element=collection_counts, 
                                           show_clear_button=False)
        mo.output.replace(select_collection_form)
    except:
        print("Database not instantiated")
    return collection_counts, df2, select_collection_form


@app.cell
def __(select_collection_form):
    if select_collection_form.value is not None:
        c_ids = select_collection_form.value.reset_index()['id'].to_list()
        c_id = -1
        if len(select_collection_form.value) > 0:
            c_id = select_collection_form.value.reset_index().iloc[0]['id']
    return c_id, c_ids


@app.cell
def __(c_ids, select_collection_form):
    if select_collection_form.value is not None:

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

        q2_study_types = """
        SELECT DISTINCT skc.name, ske.id, ske.content, ske.publication_date as pub_date, ske.type as pub_type, emb.embedding, skf.content, n.content
        FROM langchain_pg_embedding as emb, 
            "ScientificKnowledgeExpression" as ske,
            "ScientificKnowledgeCollection_has_members" as skc_hm, 
            "ScientificKnowledgeCollection" as skc, 
            "ScientificKnowledgeFragment" as skf,
            "Note" as n,
            "Note_is_about" as nia
        WHERE n.type = 'TiAbClassificationNote__cryoet_study_types' AND
            n.id = nia."Note_id" AND
            nia.is_about_id = ske.id AND
            emb.cmetadata->>'i_type' = 'CitationRecord' AND
            emb.cmetadata->>'e_id' = ske.id AND 
            emb.cmetadata->>'f_id' = skf.id AND
            skc_hm."ScientificKnowledgeCollection_id" = skc.id AND
            ske.id = skc_hm.has_members_id AND ({})
        ORDER BY pub_date DESC;
        """.format(collections_clause)

        q2_background = """
        SELECT DISTINCT skc.name, ske.id, ske.content, ske.publication_date as pub_date, ske.type as pub_type, emb.embedding, n.content 
        FROM langchain_pg_embedding as emb, 
            "ScientificKnowledgeExpression" as ske,
            "ScientificKnowledgeCollection_has_members" as skc_hm,
            "ScientificKnowledgeCollection" as skc, 
            "Note" as n
        WHERE emb.cmetadata->>'n_type' = 'TiAbMappingNote__Discourse' AND
            emb.cmetadata->>'about_id' = ske.id AND 
            emb.cmetadata->>'discourse_type' = 'Background' AND 
            emb.cmetadata->>'n_id' = n.id AND 
            skc_hm."ScientificKnowledgeCollection_id" = skc.id AND
            ske.id = skc_hm.has_members_id AND ({})
        ORDER BY pub_date DESC;
        """.format(collections_clause)

        q2_objectives_methods = """
        SELECT DISTINCT skc.name, ske.id, ske.content, ske.publication_date as pub_date, ske.type as pub_type, emb.embedding, n.content 
        FROM langchain_pg_embedding as emb, 
            "ScientificKnowledgeExpression" as ske,
            "ScientificKnowledgeCollection_has_members" as skc_hm,
            "ScientificKnowledgeCollection" as skc, 
            "Note" as n
        WHERE emb.cmetadata->>'n_type' = 'TiAbMappingNote__Discourse' AND
            emb.cmetadata->>'about_id' = ske.id AND 
            emb.cmetadata->>'discourse_type' = 'ObjectivesMethods' AND 
            emb.cmetadata->>'n_id' = n.id AND 
            skc_hm."ScientificKnowledgeCollection_id" = skc.id AND
            ske.id = skc_hm.has_members_id AND ({})
        ORDER BY pub_date DESC;
        """.format(collections_clause)

        q2_results_conclusions = """
        SELECT DISTINCT skc.name, ske.id, ske.content, ske.publication_date as pub_date, ske.type as pub_type, emb.embedding, n.content
        FROM langchain_pg_embedding as emb, 
        """.format(collections_clause)
    return (
        collections_clause,
        q2_all,
        q2_background,
        q2_objectives_methods,
        q2_results_conclusions,
        q2_study_types,
    )


@app.cell
def __(
    mo,
    q2_all,
    q2_background,
    q2_objectives_methods,
    q2_results_conclusions,
    q2_study_types,
    select_collection_form,
    set_prunelist,
):
    if select_collection_form.value is not None:
        map_type_dropdown = mo.ui.dropdown(
            options={"All papers": ('All', q2_all), 
                     "Study Types": ('StudyTypes', q2_study_types), 
                     "Background": ('Background', q2_background), 
                     "Objectives + Methods": ('ObjectivesMethods', q2_objectives_methods), 
                     "Results + Conclusions": ('ResultsConclusions', q2_results_conclusions)},
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
        mo.output.replace(mo.vstack([map_type_dropdown, paper_type_table]))
    return map_type_dropdown, paper_type_table


@app.cell
def __(
    get_prunelist,
    mo,
    rag_data,
    select_collection_form,
    selected_dois,
    set_prunelist,
):
    if select_collection_form.value is not None:

        l = get_prunelist()
        prune_pb = mo.ui.button(label='Prune', value=selected_dois+l, on_click=set_prunelist)
        select_pb = mo.ui.button(label='Select', 
                                 on_click=set_prunelist, 
                                 value=[tup[1] for tup in rag_data if tup[1] not in selected_dois or tup[1] in l])
        clear_pb = mo.ui.button(label='Reset', on_click=set_prunelist, value=[])
        spr_buttons = mo.hstack([select_pb, prune_pb, clear_pb], justify="center")
        mo.output.replace(mo.left(spr_buttons))
    return clear_pb, l, prune_pb, select_pb, spr_buttons


@app.cell
def __(embed_df, mo, select_collection_form):
    if select_collection_form.value is not None:

        start_slider = mo.ui.slider(label='start', \
                          start=embed_df['date'].min().year, \
                          stop=embed_df['date'].max().year) 
        end_slider = mo.ui.slider(label='end', \
                          start=embed_df['date'].min().year, \
                          stop=embed_df['date'].max().year, \
                          value=embed_df['date'].max().year)
    return end_slider, start_slider


@app.cell
def __(end_slider, mo, select_collection_form, start_slider):
    if select_collection_form.value is not None:

        start_value = mo.ui.text(value=str(start_slider.value), disabled=True )
        end_value = mo.ui.text(value=str(end_slider.value), disabled=True )

        mo.output.replace(mo.vstack([
            mo.left(mo.hstack([start_slider, start_value])),
            mo.left(mo.hstack([end_slider, end_value]))]))
    return end_value, start_value


@app.cell
def __(c_ids, embed_df, end_slider, start_slider):
    if len(c_ids) > 0:
        embedding_df = embed_df[
            (embed_df.date.dt.year>=start_slider.value) & 
            (embed_df.date.dt.year<=end_slider.value)]
    return embedding_df,


@app.cell
def __(alt, embedding_df, mo, select_collection_form):
    if select_collection_form.value is not None:

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
        mo.output.replace(chart)
    return chart,


@app.cell
def __(ldb, map_type_dropdown, select_collection_form, text):
    if select_collection_form.value is not None:

        map_type = map_type_dropdown.value[0]
        map_type_query = map_type_dropdown.value[1]
        ldb.session.rollback()
        rag_data = ldb.session.execute(text(map_type_query)).fetchall()
    return map_type, map_type_query, rag_data


@app.cell
def __():
    import platform; 
    print(platform.platform())
    return platform,


@app.cell
def __(
    compute_embedding,
    get_prunelist,
    json,
    map_type,
    mo,
    paper_type_table,
    pd,
    pymde,
    rag_data,
    re,
    select_collection_form,
    study_type_lookup,
    torch,
):
    if select_collection_form.value is not None:

        rag_coll_list = []
        rag_id_list = []
        rag_url_list = []
        rag_ref_list = []
        rag_date_list = []
        rag_type_list = []
        rag_text_list = []
        rag_embeddings_list = []
        for tup in rag_data: 
            cid, eid, ref, date, ptype, embed, txt = tup[0:7]
            dat = None
            if len(tup) == 8:
                print(tup[7])
                dat = json.loads(tup[7]) 
                cid = study_type_lookup.get(dat.get('cryoet_study_type_code'), 'X')
            if eid in get_prunelist():
                #print(eid)
                continue
            if (ptype in paper_type_table.value) is False:
                #print(txt)
                continue
            doi = re.sub('doi:', '', eid)
            doi_html = mo.Html('<a href="https://doi.org/'+doi+'">'+doi+'</a>')
            rag_coll_list.append(cid)    
            rag_id_list.append(eid)
            rag_url_list.append(doi_html)
            rag_ref_list.append(ref)
            rag_date_list.append(date)
            rag_type_list.append(ptype)
            rag_embeddings_list.append(json.loads(embed))
            rag_text_list.append(txt)

        rag_embeddings_tensor = torch.FloatTensor(rag_embeddings_list)

        embedding_dimension = 2
        constraint = pymde.Standardized()
        embedding = compute_embedding(rag_embeddings_tensor, embedding_dimension, constraint)

        if map_type == "Background" or map_type == 'ObjectivesMethods' or map_type == 'ResultsConclusions':
            rag_text_list = [json.loads(r).get(map_type) for r in rag_text_list]

        embedding_sampled = embedding.cpu()
        embed_df = pd.DataFrame(
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
        embed_df["date"] = pd.to_datetime(embed_df["date"])
    return (
        cid,
        constraint,
        dat,
        date,
        doi,
        doi_html,
        eid,
        embed,
        embed_df,
        embedding,
        embedding_dimension,
        embedding_sampled,
        ptype,
        rag_coll_list,
        rag_date_list,
        rag_embeddings_list,
        rag_embeddings_tensor,
        rag_id_list,
        rag_ref_list,
        rag_text_list,
        rag_type_list,
        rag_url_list,
        ref,
        tup,
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
            device="cpu",
            verbose=True,
        )
        X = mde.embed(verbose=True)
        mo.output.clear()
        return X
    return compute_embedding,


@app.cell
def __(alt, mo, papers_df, pd, resample_dropdown, select_collection_form):
    def to_altair_datetime(dt):
        dt = pd.to_datetime(dt)
        return alt.DateTime(year=dt.year, month=dt.month, date=dt.day,
                            hours=dt.hour, minutes=dt.minute, seconds=dt.second,
                            milliseconds=0.001 * dt.microsecond)

    if select_collection_form.value is not None:

        time_domain = [to_altair_datetime('2010-01-01'),
                  to_altair_datetime('2024-06-01')]

        ts_df = papers_df.set_index('date') \
                .groupby('Collection') \
                .resample(resample_dropdown.value) \
                .count() \
                .drop(columns=['Reference', 'Type', 'Collection']) \
                .rename(columns={'DOI': 'Monthly Publication Count'}) \
                .reset_index(drop=False)
        chart3 = alt.Chart(ts_df, width="container").mark_point().encode(
            x=alt.X('date:T'),#.scale(domain=time_domain),
            y='Monthly Publication Count',
            color='Collection'
        )

        c = chart3 + chart3.transform_loess('date', 'Monthly Publication Count', groupby=['Collection']).mark_line()
        mo.output.replace(c)
    return c, chart3, time_domain, to_altair_datetime, ts_df


@app.cell
def __(mo, select_collection_form):
    if select_collection_form.value is not None:    
        resample_dropdown = mo.ui.dropdown(
          options=['1M', '2M', '3M', '6M', '1Y'],
          value='3M',
          label='Sampling Interval'
        )
        mo.output.replace(resample_dropdown)
    return resample_dropdown,


@app.cell
<<<<<<< HEAD
def __(chart, embedding_df, ldb, select_collection_form):
=======
def __(chart, embedding_df, ldb, mo, select_collection_form):
>>>>>>> 75dc97aff9dc932799675920edfaed089bf106a3
    if select_collection_form.value is not None:

        ldb.session.rollback()
        if len(chart.value) > 0:
            papers_df = chart.value.drop(columns=["x", "y", "text"])
        else:
            papers_df = embedding_df.drop(columns=["x", "y", "text"])

        papers_list = [r.to_dict() for i, r in papers_df.iterrows()]
        htmls = []
        for r in papers_list:
            doi2 = r['DOI']
            r['DOI'] = mo.Html('<a href="https://doi.org/'+doi2+'" target="_blank">'+doi2+'</a>')
    return doi2, htmls, papers_df, papers_list, r


@app.cell
def __(mo, papers_df, papers_list, select_collection_form):
    if select_collection_form.value is not None:
        mo.output.replace(mo.ui.table(papers_list))
        selected_dois = [row.DOI for i, row in papers_df.iterrows()]
    return selected_dois,


@app.cell
def __(mo):
    get_prunelist, set_prunelist = mo.state([])
    return get_prunelist, set_prunelist


if __name__ == "__main__":
    app.run()
