from __init__ import *
from llama_index.llms.openai import OpenAI

#把key和url换成自己的明文key和url先试试能不能运行，不要翻墙
response = OpenAI(temperature=0, model="gpt-4o",
    api_key=OPENAI_API_KEY,
    api_base=OPENAI_BASE_URL).complete("Paul Graham is ")
print(response)