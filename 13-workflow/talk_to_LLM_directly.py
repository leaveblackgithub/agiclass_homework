import nest_asyncio
nest_asyncio.apply()
from __init__ import *
import Agently
agent = (
    Agently.create_agent()
        .set_settings("current_model", "OAIClient")
        .set_settings("model.OAIClient.url", OPENAI_BASE_URL)
        .set_settings("model.OAIClient.auth", { "api_key": OPENAI_API_KEY })
        .set_settings("model.OAIClient.options", { "model": 'deepseek-chat' })
)

result = agent.input(input("[请输入您的要求]: ")).start()
print("[回复]: ", result)