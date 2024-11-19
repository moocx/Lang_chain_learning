"""
本文件是【LangChain系统安装和快速入门】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388069981520724003

OpenAI的Completions API已经在2023年7月完成最后一次更新并废弃，该接口仅适用于早期版本的少量模型("gpt-3.5-turbo-instruct", "davinci-002", "babbage-002")；
相关功能可以被ChatCompletion接口替代。详情可见 https://platform.openai.com/docs/guides/completions。
Doubao API兼容最新版本的API调用，对废弃接口不再支持，本文件代码仅做示意。
"""

import os
from openai import OpenAI

# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
# os.environ["OPENAI_BASE_URL"] = 'OpenAI 的 API URL'

client = OpenAI()

response = client.completions.create(
    model=os.environ.get("LLM_MODELEND"),
    temperature=0.5,
    max_tokens=100,
    prompt="请给我的花店起个名",
)

print(response.choices[0].text.strip())
