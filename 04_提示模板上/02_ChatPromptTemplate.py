"""
本文件是【提示工程（上）：用少样本FewShotTemplate和ExampleSelector创建应景文案】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388069971579895818
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
""" 
# 导入聊天消息类模板
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 模板的构建
template = "你是一位专业顾问，负责为专注于{product}的公司起名。"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "公司主打产品是{product_detail}。"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
prompt_template = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

# 格式化提示消息生成提示
prompt = prompt_template.format_prompt(
    product="鲜花装饰", product_detail="创新的鲜花设计。"
).to_messages()

# 下面调用模型，把提示消息传入模型，生成结果
import os

# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'

from langchain_openai import ChatOpenAI

chat = ChatOpenAI(
    model=os.environ.get("LLM_MODELEND"),
)
result = chat(prompt)
print(result)
