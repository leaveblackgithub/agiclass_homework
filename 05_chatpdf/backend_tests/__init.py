import sys
import os

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__)) #表示当前路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #表示上一级目录
sys.path.insert(0,os.path.join(BASE_DIR,"backend"))  #也可以用os.path.join(BASE_DIR,'/lib/server')
AGI_BASE=os.getenv("AGI_BASE")
sys.path.insert(0,os.path.join(AGI_BASE,"00_shared")) 
# from backend import *
from environment_import import *

llama2="llama2"
hanyu_1_2="现代汉语（一二）-语音"
test_original_file_name="llama2"

es_search="es_search"
vd_search="vd_search"
ws_search="ws_search"

llama2_parameters="llama2_parameters"
conversation_variant="conversation_variant"
chat_version="chat_version"
commercial_license="commercial_license"
safety="safety"
safety_chn="safety_chn"

def get_dir(root_folder,*args):
    from pathlib import Path
    if not Path(Path(root_folder).root).exists(): 
        raise ValueError("Root Drive not exists")      
    result=os.path.join(root_folder,*args)
    Path(result).mkdir(parents=True, exist_ok=True)
    return result

def get_pdf_path(file_name):
    return os.path.join(RESOURCE_ROOT, file_name+".pdf")

def get_txt_path(file_name):
    return os.path.join(TEMP_ROOT, file_name+".txt") 

def add_resplit_suffix(content):
    return "_".join([content, "resplit"])





# print("BASE_DIR",BASE_DIR)
# print("sys_path",sys.path)


