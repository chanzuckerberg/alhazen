# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/',
                'doc_host': 'https://chanzuckerberg.github.io/alhazen',
                'git_url': 'https://github.com/chanzuckerberg/alhazen',
                'lib_path': 'alhazen'},
  'syms': { 'alhazen.apps': {'alhazen.apps.single_paper_chatbot': ('apps.html#single_paper_chatbot', 'alhazen/apps.py')},
            'alhazen.core': { 'alhazen.core.AGENT_TYPE': ('core.html#agent_type', 'alhazen/core.py'),
                              'alhazen.core.MODEL_TYPE': ('core.html#model_type', 'alhazen/core.py'),
                              'alhazen.core.TaskInstruction': ('core.html#taskinstruction', 'alhazen/core.py'),
                              'alhazen.core.TaskInstruction.generate_llama2_prompt_template': ( 'core.html#taskinstruction.generate_llama2_prompt_template',
                                                                                                'alhazen/core.py'),
                              'alhazen.core.TaskInstruction.generate_prompt_template': ( 'core.html#taskinstruction.generate_prompt_template',
                                                                                         'alhazen/core.py'),
                              'alhazen.core.TaskInstruction.generate_simple_instruction': ( 'core.html#taskinstruction.generate_simple_instruction',
                                                                                            'alhazen/core.py'),
                              'alhazen.core.TaskInstructionRegistry': ('core.html#taskinstructionregistry', 'alhazen/core.py'),
                              'alhazen.core.TaskInstructionRegistry.__str__': ( 'core.html#taskinstructionregistry.__str__',
                                                                                'alhazen/core.py'),
                              'alhazen.core.TaskInstructionRegistry.deregister_instruction_template': ( 'core.html#taskinstructionregistry.deregister_instruction_template',
                                                                                                        'alhazen/core.py'),
                              'alhazen.core.TaskInstructionRegistry.get_instruction_template': ( 'core.html#taskinstructionregistry.get_instruction_template',
                                                                                                 'alhazen/core.py'),
                              'alhazen.core.TaskInstructionRegistry.load_prompts_from_yaml': ( 'core.html#taskinstructionregistry.load_prompts_from_yaml',
                                                                                               'alhazen/core.py'),
                              'alhazen.core.TaskInstructionRegistry.register_instruction_template': ( 'core.html#taskinstructionregistry.register_instruction_template',
                                                                                                      'alhazen/core.py'),
                              'alhazen.core.TaskInstructionRegistry.register_new_instruction_template': ( 'core.html#taskinstructionregistry.register_new_instruction_template',
                                                                                                          'alhazen/core.py'),
                              'alhazen.core.get_cached_gguf': ('core.html#get_cached_gguf', 'alhazen/core.py'),
                              'alhazen.core.get_langchain_embeddings': ('core.html#get_langchain_embeddings', 'alhazen/core.py'),
                              'alhazen.core.get_langchain_llm': ('core.html#get_langchain_llm', 'alhazen/core.py'),
                              'alhazen.core.get_llamaindex_llm': ('core.html#get_llamaindex_llm', 'alhazen/core.py')},
            'alhazen.tools.single_document_qa': { 'alhazen.tools.single_document_qa.LocalFileLangChainChatBot': ( 'single_document_qa.html#localfilelangchainchatbot',
                                                                                                                  'alhazen/tools/single_document_qa.py'),
                                                  'alhazen.tools.single_document_qa.LocalFileLangChainChatBot.__init__': ( 'single_document_qa.html#localfilelangchainchatbot.__init__',
                                                                                                                           'alhazen/tools/single_document_qa.py'),
                                                  'alhazen.tools.single_document_qa.LocalFileLangChainChatBot.change_directory': ( 'single_document_qa.html#localfilelangchainchatbot.change_directory',
                                                                                                                                   'alhazen/tools/single_document_qa.py'),
                                                  'alhazen.tools.single_document_qa.LocalFileLangChainChatBot.index_document': ( 'single_document_qa.html#localfilelangchainchatbot.index_document',
                                                                                                                                 'alhazen/tools/single_document_qa.py'),
                                                  'alhazen.tools.single_document_qa.LocalFileLangChainChatBot.read_one_nxml_document': ( 'single_document_qa.html#localfilelangchainchatbot.read_one_nxml_document',
                                                                                                                                         'alhazen/tools/single_document_qa.py'),
                                                  'alhazen.tools.single_document_qa.LocalFileLangChainChatBot.read_one_pdf_document': ( 'single_document_qa.html#localfilelangchainchatbot.read_one_pdf_document',
                                                                                                                                        'alhazen/tools/single_document_qa.py'),
                                                  'alhazen.tools.single_document_qa.LocalFileLangChainChatBot.run_batch_of_questions_over_each_file': ( 'single_document_qa.html#localfilelangchainchatbot.run_batch_of_questions_over_each_file',
                                                                                                                                                        'alhazen/tools/single_document_qa.py'),
                                                  'alhazen.tools.single_document_qa.LocalFileLangChainChatBot.run_gradio': ( 'single_document_qa.html#localfilelangchainchatbot.run_gradio',
                                                                                                                             'alhazen/tools/single_document_qa.py'),
                                                  'alhazen.tools.single_document_qa.get_ft_url_from_doi': ( 'single_document_qa.html#get_ft_url_from_doi',
                                                                                                            'alhazen/tools/single_document_qa.py')},
            'alhazen.tools.tiab_corpus_qa': { 'alhazen.tools.tiab_corpus_qa.FileCollectionChatBot': ( 'tiab_corpus_qa.html#filecollectionchatbot',
                                                                                                      'alhazen/tools/tiab_corpus_qa.py'),
                                              'alhazen.tools.tiab_corpus_qa.FileCollectionChatBot.__init__': ( 'tiab_corpus_qa.html#filecollectionchatbot.__init__',
                                                                                                               'alhazen/tools/tiab_corpus_qa.py'),
                                              'alhazen.tools.tiab_corpus_qa.FileCollectionChatBot.run_gradio': ( 'tiab_corpus_qa.html#filecollectionchatbot.run_gradio',
                                                                                                                 'alhazen/tools/tiab_corpus_qa.py')},
            'alhazen.utils.airtableUtils': { 'alhazen.utils.airtableUtils.AirtableUtils': ( 'airtable_utils.html#airtableutils',
                                                                                            'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils.__init__': ( 'airtable_utils.html#airtableutils.__init__',
                                                                                                     'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils._get_airtable_url': ( 'airtable_utils.html#airtableutils._get_airtable_url',
                                                                                                              'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils._get_avg_doc_agr': ( 'airtable_utils.html#airtableutils._get_avg_doc_agr',
                                                                                                             'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils._get_consensus': ( 'airtable_utils.html#airtableutils._get_consensus',
                                                                                                           'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils.build_curated_dataframe': ( 'airtable_utils.html#airtableutils.build_curated_dataframe',
                                                                                                                    'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils.build_nltk_annotation_task_from_curated_df': ( 'airtable_utils.html#airtableutils.build_nltk_annotation_task_from_curated_df',
                                                                                                                                       'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils.get_consensus_per_doc': ( 'airtable_utils.html#airtableutils.get_consensus_per_doc',
                                                                                                                  'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils.read_airtable': ( 'airtable_utils.html#airtableutils.read_airtable',
                                                                                                          'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils.send_df_to_airtable': ( 'airtable_utils.html#airtableutils.send_df_to_airtable',
                                                                                                                'alhazen/utils/airtableUtils.py'),
                                             'alhazen.utils.airtableUtils.AirtableUtils.send_records_to_airtable': ( 'airtable_utils.html#airtableutils.send_records_to_airtable',
                                                                                                                     'alhazen/utils/airtableUtils.py')},
            'alhazen.utils.curatedDataUtils': { 'alhazen.utils.curatedDataUtils.CuratedDataUtils': ( 'curated_data_utils.html#curateddatautils',
                                                                                                     'alhazen/utils/curatedDataUtils.py'),
                                                'alhazen.utils.curatedDataUtils.CuratedDataUtils.__init__': ( 'curated_data_utils.html#curateddatautils.__init__',
                                                                                                              'alhazen/utils/curatedDataUtils.py'),
                                                'alhazen.utils.curatedDataUtils.CuratedDataUtils.get_avg_doc_agr': ( 'curated_data_utils.html#curateddatautils.get_avg_doc_agr',
                                                                                                                     'alhazen/utils/curatedDataUtils.py'),
                                                'alhazen.utils.curatedDataUtils.CuratedDataUtils.get_consensus': ( 'curated_data_utils.html#curateddatautils.get_consensus',
                                                                                                                   'alhazen/utils/curatedDataUtils.py'),
                                                'alhazen.utils.curatedDataUtils.CuratedDataUtils.get_consensus_per_doc': ( 'curated_data_utils.html#curateddatautils.get_consensus_per_doc',
                                                                                                                           'alhazen/utils/curatedDataUtils.py'),
                                                'alhazen.utils.curatedDataUtils.CuratedDataUtils.get_cross_curator_comparison': ( 'curated_data_utils.html#curateddatautils.get_cross_curator_comparison',
                                                                                                                                  'alhazen/utils/curatedDataUtils.py'),
                                                'alhazen.utils.curatedDataUtils.no_maybe_yes_distance': ( 'curated_data_utils.html#no_maybe_yes_distance',
                                                                                                          'alhazen/utils/curatedDataUtils.py'),
                                                'alhazen.utils.curatedDataUtils.ordinal_distance': ( 'curated_data_utils.html#ordinal_distance',
                                                                                                     'alhazen/utils/curatedDataUtils.py')},
            'alhazen.utils.jats_text_extractor': { 'alhazen.utils.jats_text_extractor.NxmlDoc': ( 'jats_text_extractor.html#nxmldoc',
                                                                                                  'alhazen/utils/jats_text_extractor.py'),
                                                   'alhazen.utils.jats_text_extractor.NxmlDoc.__init__': ( 'jats_text_extractor.html#nxmldoc.__init__',
                                                                                                           'alhazen/utils/jats_text_extractor.py'),
                                                   'alhazen.utils.jats_text_extractor.NxmlDoc.build_enahanced_document_dataframe': ( 'jats_text_extractor.html#nxmldoc.build_enahanced_document_dataframe',
                                                                                                                                     'alhazen/utils/jats_text_extractor.py'),
                                                   'alhazen.utils.jats_text_extractor.NxmlDoc.build_simple_document_dataframe': ( 'jats_text_extractor.html#nxmldoc.build_simple_document_dataframe',
                                                                                                                                  'alhazen/utils/jats_text_extractor.py'),
                                                   'alhazen.utils.jats_text_extractor.NxmlDoc.extract_ref_dict_from_nxml': ( 'jats_text_extractor.html#nxmldoc.extract_ref_dict_from_nxml',
                                                                                                                             'alhazen/utils/jats_text_extractor.py'),
                                                   'alhazen.utils.jats_text_extractor.NxmlDoc.generate_tag_tree': ( 'jats_text_extractor.html#nxmldoc.generate_tag_tree',
                                                                                                                    'alhazen/utils/jats_text_extractor.py'),
                                                   'alhazen.utils.jats_text_extractor.NxmlDoc.get_figure_reference': ( 'jats_text_extractor.html#nxmldoc.get_figure_reference',
                                                                                                                       'alhazen/utils/jats_text_extractor.py'),
                                                   'alhazen.utils.jats_text_extractor.NxmlDoc.get_top_level_sec_tag': ( 'jats_text_extractor.html#nxmldoc.get_top_level_sec_tag',
                                                                                                                        'alhazen/utils/jats_text_extractor.py'),
                                                   'alhazen.utils.jats_text_extractor.get_ft_url_from_doi': ( 'jats_text_extractor.html#get_ft_url_from_doi',
                                                                                                              'alhazen/utils/jats_text_extractor.py')},
            'alhazen.utils.ms_nlp': { 'alhazen.utils.ms_nlp.Conversation': ('ms_nlp_utils.html#conversation', 'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.Conversation.append_message': ( 'ms_nlp_utils.html#conversation.append_message',
                                                                                            'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.Conversation.copy': ( 'ms_nlp_utils.html#conversation.copy',
                                                                                  'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.Conversation.dict': ( 'ms_nlp_utils.html#conversation.dict',
                                                                                  'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.Conversation.get_prompt': ( 'ms_nlp_utils.html#conversation.get_prompt',
                                                                                        'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.Conversation.to_gradio_chatbot': ( 'ms_nlp_utils.html#conversation.to_gradio_chatbot',
                                                                                               'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.Conversation.to_openai_api_messages': ( 'ms_nlp_utils.html#conversation.to_openai_api_messages',
                                                                                                    'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.SeparatorStyle': ( 'ms_nlp_utils.html#separatorstyle',
                                                                               'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.get_conv_template': ( 'ms_nlp_utils.html#get_conv_template',
                                                                                  'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.get_response': ('ms_nlp_utils.html#get_response', 'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.preprocess_instance': ( 'ms_nlp_utils.html#preprocess_instance',
                                                                                    'alhazen/utils/ms_nlp.py'),
                                      'alhazen.utils.ms_nlp.register_conv_template': ( 'ms_nlp_utils.html#register_conv_template',
                                                                                       'alhazen/utils/ms_nlp.py')},
            'alhazen.utils.pdf_research_article_text_extractor': { 'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlock': ( 'pdf_text_extractor.html#pymupdfblock',
                                                                                                                                       'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlock.__eq__': ( 'pdf_text_extractor.html#pymupdfblock.__eq__',
                                                                                                                                              'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlock.__init__': ( 'pdf_text_extractor.html#pymupdfblock.__init__',
                                                                                                                                                'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlock.__repr__': ( 'pdf_text_extractor.html#pymupdfblock.__repr__',
                                                                                                                                                'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlock.__str__': ( 'pdf_text_extractor.html#pymupdfblock.__str__',
                                                                                                                                               'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlockLoader': ( 'pdf_text_extractor.html#pymupdfblockloader',
                                                                                                                                             'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlockLoader.__init__': ( 'pdf_text_extractor.html#pymupdfblockloader.__init__',
                                                                                                                                                      'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlockLoader.load': ( 'pdf_text_extractor.html#pymupdfblockloader.load',
                                                                                                                                                  'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlockParser': ( 'pdf_text_extractor.html#pymupdfblockparser',
                                                                                                                                             'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlockParser.__init__': ( 'pdf_text_extractor.html#pymupdfblockparser.__init__',
                                                                                                                                                      'alhazen/utils/pdf_research_article_text_extractor.py'),
                                                                   'alhazen.utils.pdf_research_article_text_extractor.PyMuPDFBlockParser.lazy_parse': ( 'pdf_text_extractor.html#pymupdfblockparser.lazy_parse',
                                                                                                                                                        'alhazen/utils/pdf_research_article_text_extractor.py')},
            'alhazen.utils.queryTranslator': { 'alhazen.utils.queryTranslator.QueryTranslator': ( 'query_translator.html#querytranslator',
                                                                                                  'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator.__init__': ( 'query_translator.html#querytranslator.__init__',
                                                                                                           'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator._closed_quote': ( 'query_translator.html#querytranslator._closed_quote',
                                                                                                                'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator._epmc': ( 'query_translator.html#querytranslator._epmc',
                                                                                                        'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator._expand_expr': ( 'query_translator.html#querytranslator._expand_expr',
                                                                                                               'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator._plusPipe': ( 'query_translator.html#querytranslator._pluspipe',
                                                                                                            'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator._pubmed': ( 'query_translator.html#querytranslator._pubmed',
                                                                                                          'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator._simple': ( 'query_translator.html#querytranslator._simple',
                                                                                                          'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator._snowflake': ( 'query_translator.html#querytranslator._snowflake',
                                                                                                             'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator._solr': ( 'query_translator.html#querytranslator._solr',
                                                                                                        'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryTranslator.generate_queries': ( 'query_translator.html#querytranslator.generate_queries',
                                                                                                                   'alhazen/utils/queryTranslator.py'),
                                               'alhazen.utils.queryTranslator.QueryType': ( 'query_translator.html#querytype',
                                                                                            'alhazen/utils/queryTranslator.py')},
            'alhazen.utils.searchEngineUtils': { 'alhazen.utils.searchEngineUtils.EFetchQuery': ( 'search_engine_eutils.html#efetchquery',
                                                                                                  'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EFetchQuery.__init__': ( 'search_engine_eutils.html#efetchquery.__init__',
                                                                                                           'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EFetchQuery._generate_mesh_rows_from_medline_records': ( 'search_engine_eutils.html#efetchquery._generate_mesh_rows_from_medline_records',
                                                                                                                                           'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EFetchQuery._generate_rows_from_medline_records': ( 'search_engine_eutils.html#efetchquery._generate_rows_from_medline_records',
                                                                                                                                      'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EFetchQuery.execute_efetch': ( 'search_engine_eutils.html#efetchquery.execute_efetch',
                                                                                                                 'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EFetchQuery.generate_data_frame_from_id_list': ( 'search_engine_eutils.html#efetchquery.generate_data_frame_from_id_list',
                                                                                                                                   'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EFetchQuery.generate_mesh_data_frame_from_id_list': ( 'search_engine_eutils.html#efetchquery.generate_mesh_data_frame_from_id_list',
                                                                                                                                        'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.ESearchQuery': ( 'search_engine_eutils.html#esearchquery',
                                                                                                   'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.ESearchQuery.__init__': ( 'search_engine_eutils.html#esearchquery.__init__',
                                                                                                            'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.ESearchQuery._check_query_phrase': ( 'search_engine_eutils.html#esearchquery._check_query_phrase',
                                                                                                                       'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.ESearchQuery.build_query_tuples': ( 'search_engine_eutils.html#esearchquery.build_query_tuples',
                                                                                                                      'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.ESearchQuery.execute_count_query': ( 'search_engine_eutils.html#esearchquery.execute_count_query',
                                                                                                                       'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.ESearchQuery.execute_query': ( 'search_engine_eutils.html#esearchquery.execute_query',
                                                                                                                 'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.ESearchQuery.execute_query_on_website': ( 'search_engine_eutils.html#esearchquery.execute_query_on_website',
                                                                                                                            'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EuroPMCQuery': ( 'search_engine_eutils.html#europmcquery',
                                                                                                   'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EuroPMCQuery.__init__': ( 'search_engine_eutils.html#europmcquery.__init__',
                                                                                                            'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.EuroPMCQuery.run_empc_query': ( 'search_engine_eutils.html#europmcquery.run_empc_query',
                                                                                                                  'alhazen/utils/searchEngineUtils.py'),
                                                 'alhazen.utils.searchEngineUtils.NCBI_Database_Type': ( 'search_engine_eutils.html#ncbi_database_type',
                                                                                                         'alhazen/utils/searchEngineUtils.py')},
            'alhazen.utils.vector_dbs': {}}}
