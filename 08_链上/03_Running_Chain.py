""" 
本文件是【链（上）：写一篇完美鲜花推文？用SequencialChain链接不同的组件】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388070991978561588
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# 设置OpenAI API密钥
import os

# 导入所需库
from langchain import PromptTemplate, LLMChain
from langchain_openai import ChatOpenAI

# 设置提示模板
prompt = PromptTemplate(
    input_variables=["flower", "season"], template="{flower}在{season}的花语是?"
)

# 初始化大模型
llm = ChatOpenAI(model=os.environ.get("LLM_MODELEND"), temperature=0)

# 初始化链
llm_chain = LLMChain(llm=llm, prompt=prompt)

# 调用链
response = llm_chain({"flower": "玫瑰", "season": "夏季"})
print(response)

# run方法
llm_chain.run({"flower": "玫瑰", "season": "夏季"})

# predict方法
result = llm_chain.predict(flower="玫瑰", season="夏季")
print(result)

# apply方法允许您针对输入列表运行链
input_list = [
    {"flower": "玫瑰", "season": "夏季"},
    {"flower": "百合", "season": "春季"},
    {"flower": "郁金香", "season": "秋季"},
]
result = llm_chain.apply(input_list)
print(result)

# generate方法
result = llm_chain.generate(input_list)
print(result)
