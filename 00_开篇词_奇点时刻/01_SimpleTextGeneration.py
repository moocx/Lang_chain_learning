"""
本文件是【开篇词｜带你亲证AI应用开发的“奇点”时刻】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388071021892337700
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
import os
from langchain_openai import ChatOpenAI

# llm = OpenAI(model_name="gpt-3.5-turbo-instruct",max_tokens=200)
llm = ChatOpenAI(model=os.environ.get("LLM_MODELEND"))
text = llm.predict("请给我写一句情人节红玫瑰的中文宣传语")
print(text)
