import openai
import os

class Chatbot:
    def __init__(self):
        # 设置 OpenAI API 认证信息
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    def reply(self, msg):
        # 调用 OpenAI 的 GPT-3 模型生成回复消息
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=msg,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7,
        )
        # 返回生成的回复消息
        return response.choices[0].text.strip()
