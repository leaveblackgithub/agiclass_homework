from __init import *
from talk_to_gpt_4o import *
import pytest

def test_get_completion():
    assert len(get_completion("你好").strip())>0