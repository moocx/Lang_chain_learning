"""
本文件是【模型I/O：输入提示、调用模型、解析输出】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7396583376915005480
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# 导入LangChain中的提示模板
import os
from langchain.prompts import PromptTemplate

# 创建原始模板
template = """您是一位专业的鲜花店文案撰写员。\n
对于售价为 {price} 元的 {flower_name} ，您能提供一个吸引人的简短描述吗？
"""
# 根据原始模板创建LangChain提示模板
prompt = PromptTemplate.from_template(template)
# 打印LangChain提示模板的内容
print(prompt)

# 设置OpenAI API Key
# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'

# 导入LangChain中的OpenAI模型接口
from langchain_openai import OpenAI, ChatOpenAI

# 创建模型实例
# model = OpenAI(model_name='gpt-3.5-turbo-instruct')
model = ChatOpenAI(model=os.environ.get("LLM_MODELEND"))
# 输入提示
input = prompt.format(flower_name=["玫瑰"], price="50")
# 得到模型的输出
output = model.invoke(input)
# 打印输出内容
print(output)
