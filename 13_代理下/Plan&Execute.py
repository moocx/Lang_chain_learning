""" 
本文件是【代理（下）：结构化工具对话、Self-Ask with Search 以及 Plan and execute 代理】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388070985528213538
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# 设置OpenAI和SERPAPI的API密钥
import os

os.environ["SERPAPI_API_KEY"] = (
    "Your SERPAPI API KEY"
)

from langchain_experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner,
)
from langchain_openai import ChatOpenAI  # ChatOpenAI模型

# 初始化大模型
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain.chains import LLMMathChain

search = SerpAPIWrapper()
llm = ChatOpenAI(model=os.environ["LLM_MODELEND"], temperature=0)
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
    ),
]

model = ChatOpenAI(model=os.environ["LLM_MODELEND"], temperature=0)

planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

agent.run("在纽约，100美元能买几束玫瑰?")
