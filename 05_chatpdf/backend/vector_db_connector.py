# __import__('pysqlite3')
# import sys

# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb
from chromadb.config import Settings
# my_vector_db_connector.py

import chromadb
from chromadb.config import Settings

class MyVectorDBConnector:
    def __init__(self, embedding_fn, persist_directory, collection_name="demo",distance="euclidean"):
        self.embedding_fn = embedding_fn
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.client = chromadb.PersistentClient(path=persist_directory, settings=Settings(allow_reset=True))
        # self.client.reset()
        if distance=="cosine":        self.collection = self.client.get_or_create_collection(name=collection_name,metadata={"hnsw:space": "l2"})
        else:        self.collection = self.client.get_or_create_collection(name=collection_name)
    
    def add_documents(self, documents):
        # 检查并过滤已经存在的文档
        existing_texts =  self.collection.get()['documents']
        new_documents = [p for p in documents if p not in existing_texts]    
        if(len(new_documents)==0):return   
        '''向 collection 中添加文档与向量'''
        self.collection.add(
            embeddings=self.embedding_fn(new_documents),  # 每个文档的向量
            documents=new_documents,  # 文档的原文
            ids=[f"id{i+len(existing_texts)}" for i in range(len(new_documents))]  # 每个文档的 id
        )
    
    def search(self, query, top_n=3):
        '''检索向量数据库'''
        results = self.collection.query(
            query_embeddings=self.embedding_fn([query]),
            n_results=top_n
        )
        return results['documents'][0]


# class MyVectorDBConnectorInMembory:
#     def __init__(self, embedding_fn, collection_name="demo"):
#         chroma_client = chromadb.Client(Settings(allow_reset=True))

#         # 为了演示，实际不需要每次 reset()
#         chroma_client.reset()

#         # 创建一个 collection
#         self.collection = chroma_client.get_or_create_collection(
#             name=collection_name)
#         self.embedding_fn = embedding_fn

#     def add_documents(self, documents):
#         '''向 collection 中添加文档与向量'''
#         self.collection.add(
#             embeddings=self.embedding_fn(documents),  # 每个文档的向量
#             documents=documents,  # 文档的原文
#             ids=[f"id{i}" for i in range(len(documents))]  # 每个文档的 id
#         )

#     def search(self, query, top_n):
#         '''检索向量数据库'''
#         results = self.collection.query(
#             query_embeddings=self.embedding_fn([query]),
#             n_results=top_n
#         )
#         return results['documents'][0]

if __name__ == "__main__":
    
    from text_embedding_ai00 import get_embeddings
    from environment_import import TEMP_ROOT
    import os
    chromadb_path=os.path.join(TEMP_ROOT,"chromadb")
    test_vd_connector=MyVectorDBConnector(get_embeddings,chromadb_path,"DEMO")
    paragraphs = ["你好，世界！", "这是一个中文句子。"]
    test_vd_connector.add_documents(paragraphs)
    print(test_vd_connector.collection.get())
    print(test_vd_connector.search("你好", 3))
    # 获取 chromadb 的存储路径
    pass  

