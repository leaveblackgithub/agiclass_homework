import __init
from english_utils import *
import pytest
def test_english_utils():
    # 测试关键词提取
    assert to_keywords("John works at Google. He is a software engineer.")== "john work googl softwar engin"
    assert split_text(["John works at Google. He is a software engineer."]) ==['John works at Google. He is a software engineer.']
    from txt_parser_test import get_test_paragraphs_from_txt
    txt_paragraphs = get_test_paragraphs_from_txt()
    txt_paragraphs_resplit=split_text(txt_paragraphs)
    assert len(txt_paragraphs_resplit)<len(txt_paragraphs)
#     assert len(get_test_paragraphs_from_txt[1])>300
#     assert len (split_text(get_test_paragraphs_from_txt())[1] )<=300

if __name__ == '__main__':
    from txt_parser_test import get_test_paragraphs_from_txt
    # txt_paragraphs = get_test_paragraphs_from_txt()
    print([len(s.strip()) for p in get_test_paragraphs_from_txt()[:5] for s in sent_tokenize(p)])
    print([len(item) for item in get_test_paragraphs_from_txt()[:5]])
    print([len(item) for item in split_text(get_test_paragraphs_from_txt())[:5]])