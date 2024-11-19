"""
本文件是【LangChain系统安装和快速入门】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388069981520724003
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
import os
from openai import OpenAI

# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
# os.environ["OPENAI_BASE_URL"] = 'OpenAI 的 API URL'

client = OpenAI()

# text = client.invoke("请给我写一句情人节红玫瑰的中文宣传语")
response = client.chat.completions.create(
    model=os.environ.get("LLM_MODELEND"),
    messages=[
        {"role": "system", "content": "You are a creative AI."},
        {"role": "user", "content": "请给我的花店起个名"},
    ],
    temperature=0.8,
    max_tokens=600,
)

print(response.choices[0].message.content)
