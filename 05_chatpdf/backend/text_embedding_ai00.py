import requests
import json
import time

import torch.nn.functional as F

def get_embeddings(contents,dimension=4096):
    return [get_embedding(content,dimension) for content in contents]

import numpy as np

def average_pooling_single_vector(embedding, target_dim=1024):
    """
    将一个4096维的嵌入向量压缩到1024维

    参数：
    embedding (list or np.ndarray of float): 原始4096维的嵌入向量
    target_dim (int): 目标维度,默认是1024

    返回：
    np.ndarray: 压缩后的1024维嵌入向量
    """
    # 确保输入的嵌入是一个numpy数组
    embedding = np.array(embedding)
    
    # 检查输入的维度是否为4096
    assert embedding.shape[0] == 4096, "输入嵌入的维度应该为4096"
    
    # 计算压缩因子
    factor = embedding.shape[0] // target_dim
    
    # 使用平均池化进行降维
    compressed_embedding = np.mean(embedding.reshape(target_dim, factor), axis=1)
    
    return compressed_embedding



def get_embedding(content,dimension=4096):
    if dimension>4096 or dimension<1:
        raise ValueError("dimension must be between 1 and 4096")
    # 设置URL
    url = 'http://localhost:65530/api/oai/embeddings'
    
    # 设置请求头
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # 设置请求数据
    data = {
        "input": content,
        "layer": 0,
        "state": "fd7a60ed-7807-449f-8256-bccae3246222"}
    # print(data)
    
        # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))   

    # 检查响应状态
    if response.status_code != 200:
        raise ConnectionError(f"Request failed with status code {response.status_code}")
    else:
        # 手动解析 SSE 响应
        embeddings= json.loads(response.text)['data'][0]['embedding']
        if dimension==4096: return embeddings
        return average_pooling_single_vector(embeddings,dimension)
        

if "__main__" == __name__:

    from numpy_dist import l2,cos_sim
    # query = "国际争端"

    # 且能支持跨语言
    query = "global conflicts"

    documents = [
        "联合国就苏丹达尔富尔地区大规模暴力事件发出警告",
        "土耳其、芬兰、瑞典与北约代表将继续就瑞典“入约”问题进行谈判",
        "日本岐阜市陆上自卫队射击场内发生枪击事件 3人受伤",
        "国家游泳中心（水立方）：恢复游泳、嬉水乐园等水上项目运营",
        "我国首次在空间站开展舱外辐射生物学暴露实验",
    ]


    query_vec = get_embeddings([query],1)[0]
    # print(query_vec)
    # print(len(query_vec))
    doc_vecs =[get_embeddings(d,1)[0] for d in documents]
    print("Query与自己的余弦距离: {:.2f}".format(cos_sim(query_vec, query_vec)))
    print("Query与Documents的余弦距离:")
    for vec in doc_vecs:
        print(cos_sim(query_vec, vec))

    print()

    print("Query与自己的欧氏距离: {:.2f}".format(l2(query_vec, query_vec)))
    print("Query与Documents的欧氏距离:")
    distances = [l2(query_vec, vec) for vec in doc_vecs]
    sorted_docs = sorted(zip(distances, documents))
    for distance, doc in sorted_docs:
        print("Distance: {:.8f}, Document: {}".format(distance, doc))