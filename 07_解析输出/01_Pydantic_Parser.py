""" 
本文件是【输出解析：用OutputParser生成鲜花推荐列表】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388070987826364450
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# ------Part 1
import os
# os.environ["OPENAI_API_KEY"] = 'Your OpenAI API Key'

# 创建模型实例
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model=os.environ.get("LLM_MODELEND"),
)

# ------Part 2
# 创建一个空的DataFrame用于存储结果
import pandas as pd

df = pd.DataFrame(columns=["flower_type", "price", "description", "reason"])

# 数据准备
flowers = ["玫瑰", "百合", "康乃馨"]
prices = ["50", "30", "20"]

# 定义我们想要接收的数据格式
from pydantic.v1 import BaseModel, Field


class FlowerDescription(BaseModel):
    flower_type: str = Field(description="鲜花的种类")
    price: int = Field(description="鲜花的价格")
    description: str = Field(description="鲜花的描述文案")
    reason: str = Field(description="为什么要这样写这个文案")


# ------Part 3
# 创建输出解析器
from langchain.output_parsers import PydanticOutputParser

output_parser = PydanticOutputParser(pydantic_object=FlowerDescription)

# 获取输出格式指示
format_instructions = output_parser.get_format_instructions()
# 打印提示
print("输出格式：", format_instructions)


# ------Part 4
# 创建提示模板
from langchain import PromptTemplate

prompt_template = """您是一位专业的鲜花店文案撰写员。
对于售价为 {price} 元的 {flower} ，您能提供一个吸引人的简短中文描述吗？
{format_instructions}"""

# 根据模板创建提示，同时在提示中加入输出解析器的说明
prompt = PromptTemplate.from_template(
    prompt_template, partial_variables={"format_instructions": format_instructions}
)

# 打印提示
print("提示：", prompt)

# ------Part 5
for flower, price in zip(flowers, prices):
    # 根据提示准备模型的输入
    input = prompt.format(flower=flower, price=price)
    # 打印提示
    print("提示：", input)

    # 获取模型的输出
    output = model.predict(input)
    # 解析模型的输出
    parsed_output = output_parser.parse(output)
    parsed_output_dict = parsed_output.dict()  # 将Pydantic格式转换为字典

    # 将解析后的输出添加到DataFrame中
    df.loc[len(df)] = parsed_output.dict()

# 打印字典
print("输出的数据：", df.to_dict(orient="records"))
