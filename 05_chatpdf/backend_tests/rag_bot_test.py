from __init import *
import vector_db_test as vt
import es_search_test as et
from talk_to_gpt_4o_test import get_completion
from rag_bot import RAG_Bot
import pytest
import os

no_anser="我无法回答您的问题。"


def get_test_bot(search_type=es_search,is_resplit=False):
    from txt_parser_test import TestSearchConnector
    return RAG_Bot(get_completion,TestSearchConnector(search_type,is_resplit))


# def test_es_bot():
    # assert es_bot.search(test_query_of_llama2_parameters,2)[0].strip() == et.get_test_txt(et.test_txt_name_of_llmas2_parameters)[0].strip()
    # es_bot_chat=es_bot.chat_after_search(test_query_of_llama2_parameters,2)
    # assert "7B" in es_bot_chat or "70亿" in es_bot_chat 
    # assert no_anser!=es_bot_resplit.chat_after_search(test_query_commercial_license,2)
    # assert no_anser==es_bot.chat_after_search(test_query_commercial_license,2)
    # assert no_anser==es_bot.chat_after_search(test_query_of_llama2_safety,2)
    # assert no_anser!=es_bot.chat_after_reranker(test_query_of_conversation_variant, [2,5])

# def test_es_bot_chat():
#     print( get_es_bot().chat_after_search(test_query_of_conversation_variant,2))
#     print( get_es_bot().chat_after_search(test_query_of_conversation_variant,5))

# def test_vector_bot():
    # assert vector_bot.search(test_query_of_conversation_variant,5)[0].strip() == vt.get_test_txt(vt.test_txt_name_of_conversation_variant)[0].strip()
    # assert no_anser!=vector_bot.chat_after_search(test_query_commercial_license,2)
    # assert no_anser==vector_bot.chat_after_search(test_query_of_llama2_safety_chn,2)
    # assert no_anser!=vector_bot.chat_after_reranker(test_query_of_llama2_safety_chn, [2,5])

# def test_vector_bot_chat():
    # print( get_vector_bot().chat_after_search(test_query_commercial_license,5))

if __name__ == "__main__":
    # test_es_bot=get_test_bot()
    # print(test_es_bot.chat_after_search(test_querys[llama2_parameters],2))
    # print(test_es_bot.chat_after_search(test_querys[conversation_variant],2))
    # test_es_bot_resplit=get_test_bot(es_search,True)
    # print(test_es_bot_resplit.chat_after_search(test_querys[conversation_variant],2))
    # test_vd_bot=get_test_bot(vd_search)
    # print(test_vd_bot.chat_after_search(test_querys[conversation_variant],2))
    test_vd_bot_resplit=get_test_bot(vd_search,True)
    print(test_vd_bot_resplit.chat_after_search(test_querys[safety_chn],5))
    print(test_vd_bot_resplit.chat_after_reranker(test_querys[safety_chn],[5,5]))
    pass