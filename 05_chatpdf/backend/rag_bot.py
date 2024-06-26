from reranker import get_reranker
class RAG_Bot:
    prompt_template = """
    你是一个问答机器人。
    你的任务是根据下述给定的已知信息回答用户问题。

    已知信息:
    {context}

    用户问：
    {query}
    如果已知信息不包含用户问题的答案，或者已知信息不足以回答用户的问题，请直接回复"我无法回答您的问题"。
    请不要输出已知信息中不包含的信息或答案。
    请用中文回答用户问题。
    """

    def __init__(self,llm_api, search_provider):
        self.search_provider = search_provider
        self.llm_api = llm_api
        self.search_results=None
        self.prompt=None


    def build_prompt(self,**kwargs):
        '''将 Prompt 模板赋值'''
        inputs = {}
        for k, v in kwargs.items():
            if isinstance(v, list) and all(isinstance(elem, str) for elem in v):
                val = '\n\n'.join(v)
            else:
                val = v
            inputs[k] = val
        self.prompt=self.prompt_template.format(**inputs)
        return self.prompt
        

    def get_attrs(self,paragraphs,user_query):
        self.search_results=paragraphs
        self.user_query = user_query

    def search(self,user_query, search_n=2):
        self.get_attrs(self.search_provider.search(user_query,search_n),user_query)
        return self.search_results

    def chat(self):
        if self.search_results==None:
            raise RuntimeError( "请先调用search方法")
        self.build_prompt(context=self.search_results, query=self.user_query)
        self.response = self.llm_api(self.prompt)
        return self.response
    
    
    def reranker_search_result(self,reranker_n):
        self.search_results = get_reranker(self.user_query,self.search_results,reranker_n)
        return self.search_results

    
    def chat_after_search(self,user_query, search_n=2):
        self.search(user_query,search_n)
        return self.chat()
    
    def chat_after_reranker(self,user_query, search_reranker=[2,5]):
        self.search(user_query,search_reranker[1])
        self.reranker_search_result(search_reranker[0])
        return self.chat()

if __name__ == "__main__":
    pass
    # from test_consts import print_test_separation,test_es_bot,test_vector_bot,test_query_of_conversation_variant
    # print_test_separation("test_build_prompt"")
    # print(build_prompt(prompt_template, context="已知信息", query="用户问"))
    # print_test_separation("test_es_bot")
    # print(test_es_bot.chat(test_query_of_conversation_variant))
    # print_test_separation("test_vector_bot")
    # print(test_vector_bot.chat(test_query_of_conversation_variant))
    
