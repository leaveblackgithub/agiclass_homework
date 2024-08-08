from __init import *
from es_search import MyEsConnector
import pytest
import os

# def write_test_search_txt(file_query_dict,top_n=2):
#     from txt_parser_test import write_test_txt
#     for (filename,query) in file_query_dict.items():
#         write_test_txt(add_es_search_suffix(filename),
#                        get_test_es_connector().search(query, top_n), 
#                        get_test_es_connector_resplit().search(query, top_n))

test_es_connector_name="test_es_connector"
test_es_connector_resplit_name=add_resplit_suffix(test_es_connector_name)

def get_test_es_connector():    
    from txt_parser_test import get_test_paragraphs_from_txt
    global test_es_connector
    if test_es_connector_name not in globals():
        test_es_connector=MyEsConnector(test_es_connector_name)
        test_es_connector.bulk(get_test_paragraphs_from_txt())
    return test_es_connector


def get_test_es_connector_resplit():    
    from txt_parser_test import get_test_paragraphs_from_txt_resplit
    global test_es_connector_resplit
    if test_es_connector_resplit_name not in globals():
        test_es_connector_resplit=MyEsConnector(test_es_connector_resplit_name)
        test_es_connector_resplit.bulk(get_test_paragraphs_from_txt_resplit())
    return test_es_connector


def test_es_search():
    from txt_parser_test import get_test_search_txt
    assert get_test_es_connector().search(test_querys[llama2_parameters], 2)[1].strip() == \
        get_test_search_txt(llama2_parameters,es_search)[1].strip()
    assert get_test_es_connector_resplit().search(test_querys[conversation_variant], 2)[1].strip()  \
        == get_test_search_txt(llama2_parameters,es_search,True)(conversation_variant)[1].strip() 


if __name__ == '__main__':
    from test_data import *
    test_es_connector=get_test_es_connector()
    print(test_es_connector.search(TestData().query_str(llama2_parameters), 2))
    pass
    # write_test_txt(test_txt_name_of_llmas2_parameters,test_query_of_conversation_variant,2)
    # print(len(get_test_txt(test_txt_name_of_llmas2_parameters)))
    # write_test_txt(test_txt_name_of_conversation_variant,test_query_of_conversation_variant,5)
    # print(len(get_test_txt(test_txt_name_of_conversation_variant)))