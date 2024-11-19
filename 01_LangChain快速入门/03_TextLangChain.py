"""
本文件是【LangChain系统安装和快速入门】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388069981520724003
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
import os
from langchain_openai import ChatOpenAI

# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
# os.environ["OPENAI_BASE_URL"] = 'OpenAI 的 API URL'


llm = ChatOpenAI(
    model=os.environ.get("LLM_MODELEND"),
    temperature=0.8,
    max_tokens=600,
)
response = llm.predict("请给我的花店起个名")

print(response)
