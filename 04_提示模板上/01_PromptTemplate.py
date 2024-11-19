"""
本文件是【提示工程（上）：用少样本FewShotTemplate和ExampleSelector创建应景文案】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388069971579895818
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""

from langchain import PromptTemplate

template = """\
请你模拟三位出色、逻辑性强的专家合作回答一个问题。
每个人都详细地解释他们的思考过程，考虑到其他人之前的解释，并公开承认错误。在每一步，只要可能，每位专家都会在其他人的思考基础上进行完善和建设，并承认他们的贡献。他们继续，直到对问题有一个明确的答案。   
你给一个销售{product}的电商公司，提出战略定位，企业的发展规划？
"""
prompt = PromptTemplate.from_template(template)

print(prompt.format(product="交换机"))

prompt = PromptTemplate(
    input_variables=["product", "market"],
    template="你是业务咨询顾问。对于一个面向{market}市场的，专注于销售{product}的公司，你会推荐哪个名字？",
)
print(prompt.format(product="居民", market="保险"))
#TODO 调用这些prompt 生成文本