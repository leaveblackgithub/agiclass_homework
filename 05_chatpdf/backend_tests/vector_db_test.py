from __init import *
from vector_db_connector import MyVectorDBConnector
import pytest
import os

def write_test_search_txt(file_query_dict,top_n=2):
    from txt_parser_test import write_test_txt,add_vd_search_suffix
    for (filename,query) in file_query_dict.items():
        write_test_txt(add_vd_search_suffix(filename), get_test_vd_connector().search(query, top_n), 
                       get_test_vd_connector_resplit().search(query, top_n))


test_vd_connector_name="test_vd_connector"
test_vd_connector_resplit_name=add_resplit_suffix(test_vd_connector_name)
chromadb_path=get_dir(TEMP_ROOT,"chromadb")
# print (get_dir(TEMP_ROOT,"chromadb"))

def get_test_vd_connector():    
    global test_vd_connector
    from txt_parser_test import get_test_paragraphs_from_txt
    from text_embedding_ai00 import get_embeddings
    if test_vd_connector_name not in globals():
        test_vd_connector=MyVectorDBConnector(get_embeddings,chromadb_path,test_vd_connector_name)
        test_vd_connector.add_documents(get_test_paragraphs_from_txt())
    return test_vd_connector

def get_test_vd_connector_resplit():  
    global test_vd_connector_resplit
    from txt_parser_test import get_test_paragraphs_from_txt_resplit
    from text_embedding_ai00 import get_embeddings
    if test_vd_connector_resplit_name not in globals():
        test_vd_connector_resplit=MyVectorDBConnector(get_embeddings,chromadb_path,test_vd_connector_resplit_name)
        test_vd_connector_resplit.add_documents(get_test_paragraphs_from_txt_resplit())
    return test_vd_connector_resplit



def test_es_search():
    from txt_parser_test import get_test_search_txt
    assert get_test_vd_connector().search(test_querys[conversation_variant], 2)[1].strip() == \
        get_test_search_txt(conversation_variant,vd_search)[1].strip()
    assert get_test_vd_connector_resplit().search(test_querys[safety_chn], 2)[1].strip()  == \
        get_test_search_txt(safety_chn,vd_search,True)[1].strip() 
    pass

if __name__ == '__main__':
    query_list=[safety_chn,conversation_variant]
    write_test_search_txt({f:q for (f,q) in test_querys.items() if f in query_list},5)
    pass