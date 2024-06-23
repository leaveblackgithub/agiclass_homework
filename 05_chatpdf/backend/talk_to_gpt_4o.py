
from environment_import import OpenAI,client


def get_completion(prompt, model="gpt-4o"):

    # 把用户输入加入消息历史
    messages=[({"role": "user", "content": prompt})]

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

if __name__ == "__main__":
    print(get_completion("你好"))


