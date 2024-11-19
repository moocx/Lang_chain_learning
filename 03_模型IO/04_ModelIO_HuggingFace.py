"""
本文件是【模型I/O：输入提示、调用模型、解析输出】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7396583376915005480
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# 导入LangChain中的提示模板
from langchain.prompts import PromptTemplate

# 创建原始模板
template = """You are a flower shop assitiant。\n
For {price} of {flower_name} ，can you write something for me？
"""
# 根据原始模板创建LangChain提示模板
prompt = PromptTemplate.from_template(template)
# 打印LangChain提示模板的内容
print(prompt)

# 设置HuggingFace API Token
import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

from langchain_community.llms import HuggingFaceHub

# 创建模型实例
model = HuggingFaceHub(repo_id="google/flan-t5-large")
# 输入提示
input = prompt.format(flower_name=["玫瑰"], price="50")
# 得到模型的输出
output = model.invoke(input)
# 打印输出内容
print(output)
