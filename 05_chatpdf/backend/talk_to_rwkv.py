import requests
import json

def get_completion(content):
    # 设置URL
    url = 'http://127.0.0.1:8000/chat/completions'
    
    # 设置请求头
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # 设置请求数据
    data = {
        "frequency_penalty": 1,
        "max_tokens": 1000,
        "messages": [
            {
                "content": content,
                "raw": False,
                "role": "user"
            }
        ],
        "model": "rwkv",
        "presence_penalty": 0,
        "presystem": True,
        "stream": False,
        "temperature": 1,
        "top_p": 0.3
    }
    
    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # 检查响应状态码
    if response.status_code == 200:
        # 提取并返回choices的message的content字段
        return response.json()['choices'][0]['message']['content']
    else:
        # 处理错误情况
        return f"Error: {response.status_code} - {response.text}"

# # 示例调用
# content = "讲个笑话吧"
# completion = get_completion(content)
# print(completion)
