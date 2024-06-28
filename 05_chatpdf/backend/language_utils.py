import re
import jieba
import jieba.analyse
import nltk
from rake_nltk import Rake

# 下载 punkt 数据包
nltk.download('punkt')

def is_chinese(char):
    return '\u4e00' <= char <= '\u9fff'

def is_english(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'

def is_pinyin(word):
    pinyin_pattern = re.compile(r"^[a-zA-ZüÜ]+[1-4]?$")
    return pinyin_pattern.match(word) is not None

def split_text_by_language(text):
    chinese_text = []
    english_text = []
    pinyin_text = []
    
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    
    for sentence in sentences:
        chinese_part = []
        english_part = []
        pinyin_part = []
        
        words = sentence.split()
        for word in words:
            if all(is_chinese(char) for char in word):
                chinese_part.append(word)
            elif all(is_english(char) for char in word):
                english_part.append(word)
            elif is_pinyin(word):
                pinyin_part.append(word)
            else:
                english_part.append(word)  # 默认处理为英文单词
        
        if chinese_part:
            chinese_text.append(' '.join(chinese_part))
        if english_part:
            english_text.append(' '.join(english_part))
        if pinyin_part:
            pinyin_text.append(' '.join(pinyin_part))
    
    return ' '.join(chinese_text), ' '.join(english_text), ' '.join(pinyin_text)

def extract_keywords(text, language, top_k=5):
    if language == 'chinese':
        keywords = jieba.analyse.extract_tags(text, topK=top_k, withWeight=False)
    elif language == 'pinyin':
        rake = Rake()
        rake.extract_keywords_from_text(text)
        keywords = rake.get_ranked_phrases()[:top_k]
    elif language == 'english':
        rake = Rake()
        rake.extract_keywords_from_text(text)
        keywords = rake.get_ranked_phrases()[:top_k]
    else:
        keywords = []
    
    return keywords

# 测试文本
test_text = "你好，这是一个测试。Hello, this is a test. ni hao, zhe shi yi ge ce shi."

# 拆分文本
chinese_text, english_text, pinyin_text = split_text_by_language(test_text)

# 句子分割
chinese_sentences = nltk.sent_tokenize(chinese_text)
english_sentences = nltk.sent_tokenize(english_text)
pinyin_sentences = nltk.sent_tokenize(pinyin_text)

# 提取关键词
chinese_keywords = extract_keywords(' '.join(chinese_sentences), 'chinese')
english_keywords = extract_keywords(' '.join(english_sentences), 'english')
pinyin_keywords = extract_keywords(' '.join(pinyin_sentences), 'pinyin')

print("Chinese Text:", chinese_text)
print("English Text:", english_text)
print("Pinyin Text:", pinyin_text)

print("Chinese Sentences:", chinese_sentences)
print("English Sentences:", english_sentences)
print("Pinyin Sentences:", pinyin_sentences)

print("Chinese Keywords:", chinese_keywords)
print("English Keywords:", english_keywords)
print("Pinyin Keywords:", pinyin_keywords)
