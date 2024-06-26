from elasticsearch7 import Elasticsearch, helpers
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import re


import warnings
warnings.simplefilter("ignore")  # 屏蔽 ES 的一些Warnings

# 实验室平台已经内置
#nltk.download('punkt')  # 英文切词、词根、切句等方法
#nltk.download('stopwords')  # 英文停用词库
def to_keywords(input_string):
    '''（英文）文本只保留关键字'''
    # 使用正则表达式替换所有非字母数字的字符为空格
    no_symbols = re.sub(r'[^a-zA-Z0-9\s]', ' ', input_string)
    word_tokens = word_tokenize(no_symbols)
    # 加载停用词表
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    # 去停用词，取词根
    filtered_sentence = [ps.stem(w)
                         for w in word_tokens if not w.lower() in stop_words]
    return ' '.join(filtered_sentence)


def split_text(paragraphs, chunk_size=300, overlap_size=100):
    from text_resplit import split_text
    return split_text(paragraphs,sent_tokenize, chunk_size=chunk_size, overlap_size=overlap_size)

if "__main__" == __name__:
    # 测试关键词提取
    print(to_keywords("John works at Google. He is a software engineer."))
    print(to_keywords("How many paramters does llama 2 have"))
    print(split_text(["John works at Google. He is a software engineer."]))