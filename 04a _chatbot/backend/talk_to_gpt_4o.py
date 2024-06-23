
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# 从系统参数位置加载 .env 文件
env_path = os.getenv('ENV_PATH')
load_dotenv(dotenv_path=env_path)
# 从本地加载.env文件
#_ = load_dotenv(find_dotenv())

client = OpenAI()

# 定义消息历史。先加入 system 消息，里面放入对话内容以外的 prompt
messages = [
    {
        "role": "system",
        "content": "你好，我是DDN编写的聊天机器人。请问有什么可以帮助您的？"
    }
]

def get_completion(prompt, model="gpt-4o"):

    # 把用户输入加入消息历史
    messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
    except Exception as e:
        msg = "服务器不可用，请联系agiclass技术人员检查后台信息"
    else:
        msg = response.choices[0].message.content

    # 把模型生成的回复加入消息历史。很重要，否则下次调用模型时，模型不知道上下文
    messages.append({"role": "assistant", "content": msg})
    return msg






if __name__ == '__main__':
    print(get_completion("你好"))