import os
from __init import *
from pdf_parser import extract_text_from_pdf
import pytest

test_pdf_paragraphs_name="test_pdf_paragraphs"

def get_test_paragraphs_from_pdf(file_name):    
    global test_pdf_paragraphs
    if test_pdf_paragraphs_name not in globals(): test_pdf_paragraphs={}
    if file_name not in test_pdf_paragraphs.keys():
        test_pdf_paragraphs[file_name]= extract_text_from_pdf(get_pdf_path(file_name), min_line_length=10)
    return test_pdf_paragraphs[file_name]
    

def test_extract_text_from_pdf():
    assert len(get_test_paragraphs_from_pdf(llama2))==125
    assert len(get_test_paragraphs_from_pdf(hanyu_1_2))==238


if __name__ == '__main__':
    print(get_test_paragraphs_from_pdf(llama2))
    print(get_test_paragraphs_from_pdf(hanyu_1_2))
