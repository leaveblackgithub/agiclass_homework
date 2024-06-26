import os
from __init import *
from english_utils import split_text as english_split_text
from chinese_utils import split_text as chinese_split_text
import pytest

def write_pdf_paragraphs_to_txt():
    from pdf_parser_test import get_test_paragraphs_from_pdf
    test_paragraphs=get_test_paragraphs_from_pdf()
    test_paragraphs_resplit=english_split_text(test_paragraphs)
    write_test_txt(test_original_file_name, test_paragraphs,test_paragraphs_resplit)
    test_paragraphs=get_test_paragraphs_from_pdf(True)
    test_paragraphs_resplit=chinese_split_text(test_paragraphs)
    write_test_txt(test_original_file_chn_name, test_paragraphs,test_paragraphs_resplit)



def write_test_txt(file_name, data,data_resplit):
    from txt_parser import write_to_txt
    write_to_txt(get_txt_path(file_name), data)
    write_to_txt(get_txt_path(add_resplit_suffix(file_name)), data_resplit)

def get_test_txt(file_name):
    from txt_parser import read_from_txt
    # write_to_txt(test_txt_path, data)
    return read_from_txt(get_txt_path(file_name))

def get_test_txt_resplit(file_name):
    from txt_parser import read_from_txt
    # write_to_txt(test_txt_path, data)
    return read_from_txt(get_txt_path(add_resplit_suffix(file_name)))


def get_test_paragraphs_from_txt():
    test_paragraphs_name="test_paragraphs"
    global test_paragraphs
    if test_paragraphs_name not in globals():
        test_paragraphs=get_test_txt(test_original_file_name)
    return test_paragraphs

def get_test_paragraphs_from_txt_resplit():
    test_paragraphs_resplit_name="test_paragraphs_resplit"
    global test_paragraphs_resplit
    if test_paragraphs_resplit_name not in globals():
        test_paragraphs_resplit= get_test_txt_resplit(test_original_file_name)
    return test_paragraphs_resplit

test_search_results_name="test_search_results"

def get_test_search_txt(file_name,search_type=es_search,is_resplit=False):
    global test_search_results
    file_name="_".join([file_name,search_type])
    if(is_resplit):
        file_name=add_resplit_suffix(file_name)
    if test_search_results_name not in globals():
        test_search_results={}
    if file_name not in test_search_results.keys():
        test_search_results[file_name]=get_test_txt(file_name)  
    return test_search_results[file_name]


class TestSearchConnector:
    def __init__(self,search_type=es_search,is_resplit=False):
        self.search_type=search_type
        self.is_resplit=is_resplit
        pass

    def search(self,query_string, top_n=2):
        from txt_parser_test import get_test_search_txt
        search_key=get_query_key(query_string)
        test_search_txt=get_test_search_txt(search_key,self.search_type,self.is_resplit)
        if(len(test_search_txt)<top_n):
            print (f"Warning: the test search result is less than top_n, the search result is: \n{test_search_txt}")
            return test_search_txt
        return test_search_txt[:top_n]
    
def test_test_search_connector():
    from txt_parser_test import get_test_search_txt,TestSearchConnector
    test_es_searcher=TestSearchConnector(es_search)
    assert test_es_searcher.search(test_querys[llama2_parameters], 2)[1].strip() == \
        get_test_search_txt(llama2_parameters,es_search)[1].strip()
    test_es_searcher_resplit=TestSearchConnector(es_search,True)
    assert test_es_searcher_resplit.search(test_querys[conversation_variant], 2)[1].strip()  \
        == get_test_search_txt(conversation_variant,es_search,True)[1].strip()
    test_vd_searcher=TestSearchConnector(vd_search)
    assert test_vd_searcher.search(test_querys[conversation_variant], 2)[1].strip() == \
        get_test_search_txt(conversation_variant,vd_search)[1].strip()
    test_vd_searcher_resplit=TestSearchConnector(vd_search,True)
    assert test_vd_searcher_resplit.search(test_querys[safety_chn], 2)[1].strip()  == \
        get_test_search_txt(safety_chn,vd_search,True)[1].strip()
    pass

# def test_extract_read_from_csv():
#     # Define the path to the test PDF file

#     # Extract text from the test PDF
#     paragraphs = get_test_paragraphs_from_csv()

#     # Assert that the correct number of paragraphs is extracted
#     assert len(paragraphs) == 125

#     # Add more assertions to validate the extracted paragraphs
#     assert paragraphs[0] == get_test_paragraphs()[0]
#     assert paragraphs[1] ==  get_test_paragraphs()[1]
#     assert paragraphs[2] == get_test_paragraphs()[2]

if __name__ == '__main__':
    write_pdf_paragraphs_to_txt()
    # print(len(get_test_paragraphs_from_txt()))
    # print(len(get_test_paragraphs_from_txt_resplit()))
    # print (get_test_search_txt(llama2_parameters,es_search))
