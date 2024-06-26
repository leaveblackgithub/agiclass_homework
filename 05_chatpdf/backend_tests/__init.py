import sys
import os

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__)) #表示当前路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #表示上一级目录
sys.path.insert(0,os.path.join(BASE_DIR,"backend"))  #也可以用os.path.join(BASE_DIR,'/lib/server')
# from backend import *
from environment_import import *

test_original_file_name="llama2"

test_original_file_chn_name="现代汉语（一二）-语音"
test_pdf_name=test_original_file_name+".pdf"
test_pdf_chn_name=test_original_file_chn_name+".pdf"

llama2_parameters="llama2_parameters"
conversation_variant="conversation_variant"
chat_version="chat_version"
commercial_license="commercial_license"
safety="safety"
safety_chn="safety_chn"

test_querys={llama2_parameters:"how many parameters does llama 2 have?",
             conversation_variant:"Does llama 2 have a chat version?",
             chat_version:"Does llama 2 have a conversational variant?",
             commercial_license:"Does llama 2 have a commercial license?",
             safety:"how safe is llama 2",
             safety_chn:"llama 2安全性如何"}


es_search="es_search"
vd_search="vd_search"
wh_search="wh_search"

def get_query_key(query):
    return [k for k,v in test_querys.items() if v==query][0]

def get_txt_path(file_name):
    return os.path.join(TEMP_ROOT, file_name+".txt")    

def add_resplit_suffix(content):
    return content+"_resplit"  

def add_ws_search_suffix(content):
    return content+"_ws_search"

def add_es_search_suffix(content):
    return content+"_es_search"


def add_vd_search_suffix(content):
    return content+"_vd_search"





# print("BASE_DIR",BASE_DIR)
# print("sys_path",sys.path)


