from whoosh import index
from whoosh.fields import Schema, TEXT
from whoosh import qparser
from whoosh.qparser import QueryParser
import os

class MyWhooshSearchConnector:
    def __init__(self,indexdir,keywords_fn):
        self.indexdir = indexdir
        self.schema = Schema(para_id=TEXT(stored=True),
                            content=TEXT(stored=True),
                            keywords=TEXT(stored=True ))
        self.keywords_fn = keywords_fn
        has_dir=os.path.exists(indexdir)
        
        if not has_dir: os.mkdir(indexdir) 
        if not index.exists_in(indexdir): self.ix=index.create_in(indexdir, self.schema)
        self.ix = index.open_dir(indexdir)

    def get_max_para_id(self):
        searcher = self.ix.searcher()
        query = QueryParser("para_id", self.ix.schema).parse("*")
        results = searcher.search(query, limit=None)
        if results:
            max_id = max(int(hit['para_id']) for hit in results)
        else:
            max_id = 0
        return max_id  
    def add_paragraphs(self, paragraphs):
        writer = self.ix.writer()
        searcher = self.ix.searcher()
        max_para_id = self.get_max_para_id()

        for paragraph in paragraphs:
            query = QueryParser("content", self.ix.schema).parse(paragraph)
            results = searcher.search(query)
            
            if not results:
                max_para_id += 1
                keywords = self.keywords_fn(paragraph)
                writer.add_document(para_id=str(max_para_id), content=paragraph, keywords=keywords)
        
        writer.commit()
    
    def search(self, query_str, n=5):
        searcher = self.ix.searcher()
        keywords = self.keywords_fn(query_str)
        query = QueryParser("keywords", self.ix.schema).parse(keywords)
        results = searcher.search(query, limit=n)
        if not results:
            query = QueryParser("keywords", self.ix.schema,group=qparser.OrGroup).parse(keywords)
            results = searcher.search(query, limit=n)
        return [hit['content'] for hit in results]

# # Example usage
if __name__ == "__main__":
    from english_utils import to_keywords
    indexdir = "indexdir"
    title = "Example Title"
    connector = MyWhooshSearchConnector(indexdir, to_keywords)

    new_paragraphs = ["This is the first new paragraph.", "This is the second new paragraph."]
    connector.add_paragraphs(new_paragraphs)

    search_results = connector.search("which is first paragraph?", n=2)
    for result in search_results:
        print(result)
