from __init import *

class TestData:
    def __init__(self):
        self.test_querys={llama2_parameters:"how many parameters does llama 2 have?",
                conversation_variant:"Does llama 2 have a chat version?",
                chat_version:"Does llama 2 have a conversational variant?",
                commercial_license:"Does llama 2 have a commercial license?",
                safety:"how safe is llama 2",
                safety_chn:"llama 2安全性如何"}
        self.test_pdf_paragraphs={}
        self.test_txt_paragraphs={}


    def query_str(self,query_key):
        return self.test_querys[query_key]
    
    def query_key(self,query_str):
        return [k for k,v in self.test_querys.items() if v==query_str][0]   
    
    def pdf_paragraphs(self,file_name):
        if not file_name in self.test_pdf_paragraphs:
            from pdf_parser import extract_text_from_pdf
            self.test_pdf_paragraphs[file_name]=extract_text_from_pdf(get_pdf_path(file_name))
        return self.test_pdf_paragraphs[file_name]
    
    def txt_paragraphs(self,file_name,is_resplit=False):
        if(is_resplit): file_name=add_resplit_suffix(file_name)
        if not file_name in self.test_txt_paragraphs:
            from txt_parser import read_from_txt
            paragraphs=read_from_txt(get_txt_path(file_name))
            if(is_resplit): 
                from text_resplit import resplit
                paragraphs=resplit(paragraphs)
        return self.test_pdf_paragraphs[file_name]
    
