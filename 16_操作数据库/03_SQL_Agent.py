""" 
本文件是【连接数据库：通过链和代理查询鲜花信息】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388065974408183858
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
import os
from langchain_openai import ChatOpenAI  # ChatOpenAI模型

# 连接到FlowerShop数据库
db = SQLDatabase.from_uri("sqlite:///FlowerShop.db")
# 创建OpenAI的低级语言模型（LLM）实例，这里我们设置温度为0，意味着模型输出会更加确定性
llm = ChatOpenAI(model=os.environ["LLM_MODELEND"], temperature=0, verbose=True)

# 创建SQL Agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# 使用Agent执行SQL查询
questions = [
    "哪种鲜花的存货数量最少？",
    "平均销售价格是多少？",
]

for question in questions:
    response = agent_executor.run(question)
    print(response)
