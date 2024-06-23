from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os

# 定义Schema
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(stored=True, unique=True))

# 创建索引目录
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = create_in("indexdir", schema)

# 添加文档
writer = ix.writer()
writer.add_document(title="First document", content="This is the first document we've added!", path="/a")
writer.add_document(title="Second document", content="The second one is even more interesting!", path="/b")
writer.commit()

# 搜索关键词
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    for result in results:
        print(result['title'], result['path'])
