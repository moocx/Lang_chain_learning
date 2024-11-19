"""
本文件是【模型I/O：输入提示、调用模型、解析输出】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7396583376915005480
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
from httpx import Response
from openai import OpenAI  # 导入OpenAI
import os

# openai.api_key = '你的OpenAI API Key' # API Key

prompt_text = "您是一位专业的鲜花店文案撰写员。对于售价为{}元的{}，您能提供一个吸引人的简短描述吗？"  # 设置提示

flowers = ["玫瑰", "百合", "康乃馨"]
prices = ["50", "30", "20"]

# 循环调用Text模型的Completion方法，生成文案
for flower, price in zip(flowers, prices):
    prompt = prompt_text.format(price, flower)
    # response = openai.completions.create(
    #     model="gpt-3.5-turbo-instruct",
    #     prompt=prompt,
    #     max_tokens=100
    # )
    client = OpenAI()
    response = client.chat.completions.create(
        model=os.environ.get("LLM_MODELEND"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=100,
    )

    # print(response.choices[0].text.strip()) # 输出文案
    print(response.choices[0].message.content)
