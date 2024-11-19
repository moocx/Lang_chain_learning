""" 
本文件是【部署一个鲜花网络电商的人脉工具（下）】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388070997553119282
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# 设置OpenAI API密钥

# 导入所取的库
import re
from agents.weibo_agent import lookup_V
from tools.general_tool import remove_non_chinese_fields
from tools.scraping_tool import get_data
from tools.textgen_tool import generate_letter
import os

os.environ["SERPAPI_API_KEY"] = (
    "Your SERPAPI API KEY"
)

def find_bigV(flower: str):
    # 拿到UID
    response_UID = lookup_V(flower_type=flower)

    # 抽取UID里面的数字
    UID = re.findall(r"\d+", response_UID)[0]
    print("这位鲜花大V的微博ID是", UID)

    # 根据UID爬取大V信息
    person_info = get_data(UID)
    print(person_info)

    # 移除无用的信息
    remove_non_chinese_fields(person_info)
    print(person_info)

    # 调用函数根据大V信息生成文本
    result = generate_letter(information=person_info)
    print(result)

    return result


if __name__ == "__main__":

    # 拿到UID
    response_UID = lookup_V(flower_type="牡丹")

    # 抽取UID里面的数字
    UID = re.findall(r"\d+", response_UID)[0]
    print("这位鲜花大V的微博ID是", UID)

    # 根据UID爬取大V信息
    person_info = get_data(UID)
    print(person_info)

    # 移除无用的信息
    remove_non_chinese_fields(person_info)
    print(person_info)

    result = generate_letter(information=person_info)
    print(result)

    from flask import jsonify
    import json

    # 使用json.loads将字符串解析为字典
    result = json.loads(result)
    abc = jsonify(
        {
            "summary": result["summary"],
            "facts": result["facts"],
            "interest": result["interest"],
            "letter": result["letter"],
        }
    )
