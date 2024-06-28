from __init__ import *
# get API key and create embeddings
from llama_index.embeddings.openai import OpenAIEmbedding


embed_model = OpenAIEmbedding(
    model="text-embedding-3-large",
    api_key=OPENAI_API_KEY,
    api_base=OPENAI_BASE_URL,
    dimensions=512,
)

embeddings = embed_model.get_text_embedding(
    "Open AI new Embeddings models with different dimensions is awesome."
)
print(len(embeddings))