from sentence_transformers import CrossEncoder
from environment_import import *
# model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2', max_length=512) # 英文，模型较小
def get_reranker(user_query,search_results,n_rsult=2,model_path=BGE_RERANKER_LARGE):
    model = CrossEncoder(model_path, max_length=512) # 多语言，国产，模型较大
    scores = model.predict([(user_query, doc)
                        for doc in search_results])
    # 按得分排序
    sorted_list = sorted(
        zip(scores, search_results), key=lambda x: x[0], reverse=True)
    return  [item[1] for item in sorted_list[:n_rsult]]
