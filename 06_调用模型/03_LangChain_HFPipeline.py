""" 
本文件是【调用模型：使用OpenAI API还是微调开源Llama2/ChatGLM？】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7396297142727344168
由于网络限制，Huggingface.co无法正常访问，请考虑使用国内镜像站点下载模型后、本地加载模型使用。
"""
# 指定预训练模型的名称
model = "meta-llama/Llama-2-7b-chat-hf"

# 从预训练模型中加载词汇器
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(model)

# 创建一个文本生成的管道
import transformers
import torch

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
    max_length=1000,
)

# 创建HuggingFacePipeline实例
from langchain import HuggingFacePipeline

llm = HuggingFacePipeline(pipeline=pipeline, model_kwargs={"temperature": 0})

# 定义输入模板，该模板用于生成花束的描述
template = """
              为以下的花束生成一个详细且吸引人的描述：
              花束的详细信息：
              ```{flower_details}```
           """

# 使用模板创建提示
from langchain import PromptTemplate, LLMChain

prompt = PromptTemplate(template=template, input_variables=["flower_details"])

# 创建LLMChain实例
from langchain import PromptTemplate

llm_chain = LLMChain(prompt=prompt, llm=llm)

# 需要生成描述的花束的详细信息
flower_details = "12支红玫瑰，搭配白色满天星和绿叶，包装在浪漫的红色纸中。"

# 打印生成的花束描述
print(llm_chain.run(flower_details))
