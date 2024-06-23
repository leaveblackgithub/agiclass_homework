import os
from __init import *
from pdf_parser import extract_text_from_pdf
import pytest

test_pdf_paragraphs_name="test_pdf_paragraphs"

def get_test_paragraphs_from_pdf():    
    global test_pdf_paragraphs
    # pdfName="05-rag-embedding.pdf"
    # pdfName="建筑设计防火规范(GB50016-2014)20181001修订.pdf"
    if test_pdf_paragraphs_name not in globals():
        test_pdf_path = os.path.join(CURRENT_DIR, test_pdf_name)
        test_pdf_paragraphs=    extract_text_from_pdf(test_pdf_path, min_line_length=10)
    return test_pdf_paragraphs

def test_extract_text_from_pdf():
    from  txt_parser_test import get_test_paragraphs_from_txt
    # Define the path to the test PDF file

    # Extract text from the test PDF
    paragraphs = get_test_paragraphs_from_pdf()

    # Assert that the correct number of paragraphs is extracted
    assert len(paragraphs) == 125

    # Add more assertions to validate the extracted paragraphs
    assert paragraphs[0].strip() == get_test_paragraphs_from_txt()[0].strip()
    assert paragraphs[1].strip() ==  get_test_paragraphs_from_txt()[1].strip()
    assert paragraphs[2].strip() == get_test_paragraphs_from_txt()[2].strip()


# if __name__ == '__main__':
#     # from csv_parser import write_to_csv
#     # from __init import test_csv_path
#     paragraphs = get_test_paragraphs_from_pdf()
#     print([paragraphs[0]])
