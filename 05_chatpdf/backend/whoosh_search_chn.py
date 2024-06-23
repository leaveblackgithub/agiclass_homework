from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer
import os

# 使用ChineseAnalyzer进行中文分词
analyzer = ChineseAnalyzer()

# 定义Schema
schema = Schema(title=TEXT(stored=True, analyzer=analyzer), content=TEXT(stored=True, analyzer=analyzer), path=ID(stored=True, unique=True))

# 创建索引目录
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = create_in("indexdir", schema)

# 添加文档
writer = ix.writer()
writer.add_document(title="第一个文档", content="这是我们添加的第一个文档！", path="/a")
writer.add_document(title="第二个文档", content="第二个文档更有趣！", path="/b")
writer.commit()

# 搜索关键词
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("文档")
    results = searcher.search(query)
    for result in results:
        print(result['title'], result['path'])
