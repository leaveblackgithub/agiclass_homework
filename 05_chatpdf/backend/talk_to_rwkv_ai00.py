import requests
import json
import time

def get_completion(content):
    # 设置URL
    url = 'http://localhost:65530/api/oai/chat/completions'
    
    # 设置请求头
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # 设置请求数据
    data = {
        "max_tokens": 1000,
        "messages": [
            {
                "content": content,
                "role": "user"
            }
        ],
        "names": {
            "assistant": "Assistant",
            "user": "User"
        },
        "sampler_override": {
            "frequency_penalty": 0.3,
            "penalty": 400,
            "penalty_decay": 0.99654026,
            "presence_penalty": 0.3,
            "temperature": 1,
            "top_k": 128,
            "top_p": 0.5,
            "type": "Nucleus"
        },
        "state": "fd7a60ed-7807-449f-8256-bccae3246222",
        "stop": [
            "\n\nUser:"
        ],
        "stream": True
        }
    
        # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)   

    # 检查响应状态
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
    else:
        # 手动解析 SSE 响应
        for line in response.iter_lines():
            if not line: continue
            try:
                linestr=line.decode('utf-8')
                if(linestr=='data:[DONE]' or not linestr.startswith("data:")):continue
                json_data = linestr.lstrip("data:").strip()
                data = json.loads(json_data)
                delta=data['choices'][0]['delta']
                if(not delta): continue
                content=delta.get('content')
                if(not content): continue
                print(delta.get('content'),end='',flush=True)
                time.sleep(0.05)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
                print(f"Line: {line.decode('utf-8')}")

if "__main__" == __name__:
    content = "讲个笑话吧"
    get_completion(content)