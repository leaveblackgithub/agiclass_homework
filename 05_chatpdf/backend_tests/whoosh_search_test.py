from __init import *
from whoosh_search_enu import MyWhooshSearchConnector
import pytest
import os

def write_test_search_txt(file_query_dict,top_n=2):
    from txt_parser_test import write_test_txt,add_es_search_suffix
    for (filename,query) in file_query_dict.items():
        write_test_txt(add_ws_search_suffix(filename),
                       get_test_ws_connector().search(query, top_n), 
                       get_test_ws_connector_resplit().search(query, top_n))

test_ws_connector_name="test_ws_connector"
test_ws_connector_resplit_name=add_resplit_suffix(test_ws_connector_name)
def get_index_dir(index_name):
    ws_path=os.path.join(TEMP_ROOT,wh_search)
    if not os.path.exists(ws_path): os.makedirs(ws_path)
    return os.path.join(ws_path,index_name)

def get_test_ws_connector(is_chinese=False):    
    if not is_chinese:        
        from english_utils import to_keywords
        index_name=test_original_file_name
    else: 
        from chinese_utils import to_keywords
        index_name=test_original_file_chn_name
    from txt_parser_test import get_test_paragraphs_from_txt
    global test_ws_connector
    if test_ws_connector_name not in globals():
        test_ws_connector=MyWhooshSearchConnector(get_index_dir(index_name),to_keywords)
        test_ws_connector.add_paragraphs(get_test_paragraphs_from_txt())
    return test_ws_connector


def get_test_ws_connector_resplit():    
    from txt_parser_test import get_test_paragraphs_from_txt_resplit
    global test_ws_connector_resplit
    if test_ws_connector_resplit_name not in globals():
        test_ws_connector_resplit=MyWhooshSearchConnector(ws_path,test_ws_connector_resplit_name)
        test_ws_connector_resplit.add_paragraphs(get_test_paragraphs_from_txt_resplit())
    return test_ws_connector_resplit


def test_ws_search():
    from txt_parser_test import get_test_search_txt
    assert get_test_ws_connector().search(test_querys[llama2_parameters], 2)[1].strip() == \
        get_test_search_txt(llama2_parameters,es_search)[1].strip()
    assert get_test_ws_connector_resplit().search(test_querys[conversation_variant], 2)[1].strip()  \
        == get_test_search_txt(llama2_parameters,es_search,True)(conversation_variant)[1].strip() 


if __name__ == '__main__':
    # query_list=[llama2_parameters,conversation_variant]
    # write_test_search_txt({f:q for (f,q) in test_querys.items() if f in query_list},5)
    # pass
    # write_test_txt(test_txt_name_of_llmas2_parameters,test_query_of_conversation_variant,2)
    # print(len(get_test_txt(test_txt_name_of_llmas2_parameters)))
    # write_test_txt(test_txt_name_of_conversation_variant,test_query_of_conversation_variant,5)
    # print(len(get_test_txt(test_txt_name_of_conversation_variant)))
    # print(get_test_ws_connector().search(test_querys[llama2_parameters], 2))