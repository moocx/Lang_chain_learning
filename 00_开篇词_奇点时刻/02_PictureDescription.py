"""
本文件是【开篇词｜带你亲证AI应用开发的“奇点”时刻】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388071021892337700
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# ---- Part 0 导入所需要的类
import os
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

# ---- Part I 初始化图像字幕生成模型
# 指定要使用的工具模型（HuggingFace中的image-caption模型）
hf_model = "Salesforce/blip-image-captioning-large"
print("正在初始化图像字幕生成模型...")

# 初始化处理器和工具模型
# 预处理器将准备图像供模型使用
processor = BlipProcessor.from_pretrained(hf_model)
# 然后我们初始化工具模型本身
model = BlipForConditionalGeneration.from_pretrained(hf_model)
print("初始化图像字幕生成模型成功")


# ---- Part II 定义图像字幕生成工具类
class ImageCapTool(BaseTool):
    name = "Image captioner"
    description = "使用该工具可以生成图片的文字描述，需要传入图片的URL."

    def _run(self, url: str):
        # 下载图像并将其转换为PIL对象
        image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
        # 预处理图像
        inputs = processor(image, return_tensors="pt")
        # 生成字幕
        out = model.generate(**inputs, max_new_tokens=20)
        # 获取字幕
        caption = processor.decode(out[0], skip_special_tokens=True)
        return caption

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")


# ---- PartIII 初始化并运行LangChain智能体
# llm = OpenAI(temperature=0.2)
llm = ChatOpenAI(
    model=os.environ.get("LLM_MODEL_4K_FUNCTION_CALL"),
    temperature=0,
)
print("初始化大语言模型成功")
# 使用工具初始化智能体并运行
tools = [ImageCapTool()]
agent = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
    handle_parsing_errors=True,
)

img_url = "https://lf3-static.bytednsdoc.com/obj/eden-cn/lkpkbvsj/ljhwZthlaukjlkulzlp/eec79e20058499.563190744f903.jpg"
img_arg = "https://p3-juejin-sign.byteimg.com/tos-cn-i-k3u1fbpfcp/fc9e00c57b1b45b2b06e5f8bd3aa64d6~tplv-k3u1fbpfcp-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6:q75.awebp?rk3s=bb34011d&x-expires=1730525877&x-signature=gkU%2BLF3B78pexvYBrfWLkMESZKU%3D"
# agent.run(input=f"{img_arg}\n请创作合适的中文推广文案")
agent.invoke(input=f"图片链接如下：{img_arg}\n 请为这张图创作合适的中文推广文案")
