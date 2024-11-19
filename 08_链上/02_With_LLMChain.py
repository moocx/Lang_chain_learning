""" 
本文件是【链（上）：写一篇完美鲜花推文？用SequencialChain链接不同的组件】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388070991978561588
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# 设置OpenAI API密钥
import os

# 导入所需的库
from langchain import PromptTemplate, LLMChain
from langchain_openai import ChatOpenAI

# 原始字符串模板
template = "{flower}的花语是?"
# 创建模型实例
llm = ChatOpenAI(temperature=0, model=os.environ.get("LLM_MODELEND"))
# 创建LLMChain
llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(template))
# 调用LLMChain，返回结果
result = llm_chain("玫瑰")
print(result)
