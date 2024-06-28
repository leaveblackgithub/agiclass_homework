import os
from dotenv import load_dotenv
# 从系统参数位置加载 .env 文件
env_path = os.getenv('ENV_PATH')
# print(env_path)
load_dotenv(dotenv_path=env_path)
# 从本地加载.env文件
#_ = load_dotenv(find_dotenv())

# client = OpenAI()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL')
ELASTICSEARCH_BASE_URL =  os.getenv('ELASTICSEARCH_BASE_URL')
ELASTICSEARCH_PASSWORD = os.getenv('ELASTICSEARCH_PASSWORD')
ELASTICSEARCH_NAME= os.getenv('ELASTICSEARCH_NAME')
MODEL_ROOT= os.getenv('MODEL_ROOT')
BGE_LARGE_ZH_1_5= os.path.join(MODEL_ROOT, "BAAI","bge-large-zh-v1.5")
MS_MARCO_MINILM_L_6_V2= os.path.join(MODEL_ROOT, "ms-marco-MiniLM-L-6-v2")
BGE_RERANKER_LARGE= os.path.join(MODEL_ROOT,"BAAI", "bge-reranker-large")
RESOURCE_ROOT= os.getenv('RESOURCE_ROOT')
TEMP_ROOT= os.getenv('TEMP_ROOT')

if "__main__" == __name__:
    print(env_path)
    print(BGE_RERANKER_LARGE)