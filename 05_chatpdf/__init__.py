import sys
import os

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__)) #表示当前路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #表示上一级目录
sys.path.insert(0,os.path.join(BASE_DIR,"backend"))  #也可以用os.path.join(BASE_DIR,'/lib/server')
import backend

print("BASE_DIR",BASE_DIR)
print("sys_path",sys.path)

# from es_search import *
# from vector_db_connector import *
# from text_embedding import *
# from rag_bot import *
# from talk_to_gpt_4o import *