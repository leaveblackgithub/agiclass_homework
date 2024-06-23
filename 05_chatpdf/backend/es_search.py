from elasticsearch7 import Elasticsearch, helpers
import time
from english_utils import to_keywords
from environment_import import ELASTICSEARCH_BASE_URL, ELASTICSEARCH_PASSWORD, ELASTICSEARCH_NAME

class MyEsConnector:
    def __init__(self,  index_name="teacher_demo_index"):
        # 1. 创建Elasticsearch连接
        self.es = Elasticsearch(
            hosts=[ELASTICSEARCH_BASE_URL],  # 服务地址与端口
            http_auth=(ELASTICSEARCH_NAME, ELASTICSEARCH_PASSWORD),  # 用户名，密码
        )
        # 2. 定义索引名称
        self.index_name = index_name

        # 3. 如果索引已存在，删除它（仅供演示，实际应用时不需要这步）
        if self.es.indices.exists(index=self.index_name):
            self.es.indices.delete(index=self.index_name)

        # 4. 创建索引
        self.es.indices.create(index=self.index_name)


    def bulk(self,paragraphs):

        # 5. 灌库指令
        actions = [
            {
                "_index": self.index_name,
                "_source": {
                    "keywords": to_keywords(para),
                    "text": para
                }
            }
            for para in paragraphs
        ]

        # 6. 文本灌库
        helpers.bulk(self.es, actions)

        # 灌库是异步的
        time.sleep(2)

    def search(self,query_string, top_n=2):
        # ES 的查询语言
        search_query = {
            "match": {
                "keywords": to_keywords(query_string)
            }
        }
        res = self.es.search(index=self.index_name, query=search_query, size=top_n)
        return [hit["_source"]["text"] for hit in res["hits"]["hits"]]
