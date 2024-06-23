from __init import *
from text_embedding_openai import *
import pytest

def test_get_embedding():
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

    query_vec = get_embeddings([query])[0]
    doc_vecs = get_embeddings(documents)

    cos_dist_self=cos_sim(query_vec, query_vec)

    print("Query与自己的余弦距离: {:.2f}".format(cos_dist_self))
    assert cos_dist_self == 1.0
    print("Query与Documents的余弦距离:")
    cos_dist_doc=[]
    for vec in doc_vecs:
        cost_dist=cos_sim(query_vec, vec)
        cos_dist_doc.append(cost_dist)
        print(cost_dist)

    for (cos_dist,expect) in zip(cos_dist_doc,[0.76,0.75,0.74,0.70,0.72]):
        assert cos_dist>expect

    print()

    l2_dist_self=l2(query_vec, query_vec)
    assert l2_dist_self == 0.0
    print("Query与自己的欧氏距离: {:.2f}".format(l2_dist_self))
    l2_dist_doc=[]
    print("Query与Documents的欧氏距离:")
    for vec in doc_vecs:
        l2_dist=l2(query_vec, vec)
        l2_dist_doc.append(l2_dist)
        print(l2_dist)

    for (l2_dist,expect) in zip(l2_dist_doc,[0.69,0.70,0.72,0.77,0.75]):
        assert l2_dist<expect

if __name__ == '__main__':
    test_get_embedding()
    pass