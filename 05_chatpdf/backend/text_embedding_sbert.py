from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_to_numpy, numpy_to_embedding

# 加载预训练的中文SBERT模型
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 示例文本
texts = ["你好，世界！", "这是一个中文句子。"]

# 生成嵌入
embeddings = model.encode(texts)

# 连接到ChromaDB
client = chromadb.Client(chromadb.Settings(persist_directory="path_to_chromadb_directory"))

# 创建集合
collection_name = "text_embeddings"
if not client.has_collection(collection_name):
    collection = client.create_collection(name=collection_name, embedding_type="float32", dimension=768)
else:
    collection = client.get_collection(collection_name)

# 插入数据
for text, embedding in zip(texts, embeddings):
    doc_id = collection.insert({"embedding": numpy_to_embedding(embedding), "text": text})

# 搜索示例
query_embedding = model.encode("你好")
query_embedding = numpy_to_embedding(query_embedding)
results = collection.query(query_embedding, limit=3)

# 输出搜索结果
for result in results:
    print(f"Text: {result['text']}, Score: {result['score']}")
