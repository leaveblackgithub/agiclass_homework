from __init import *
from reranker import *
import pytest

if __name__ == "__main__":
    from txt_parser_test import *
    paragraphs=get_test_txt(add_resplit_suffix(add_vd_search_suffix(safety_chn)))
    print(paragraphs)
    print()
    print(get_reranker(test_querys[safety_chn],paragraphs,2))
    pass