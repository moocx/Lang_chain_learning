""" 
本文件是【回调函数：在 AI 应用中引入异步通信机制】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388071000543346688
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
def compute(x, y, callback):
    result = x + y
    callback(result)


def print_result(value):
    print(f"The result is: {value}")


def square_result(value):
    print(f"The squared result is: {value**2}")


# 使用print_result作为回调
compute(3, 4, print_result)  # 输出: The result is: 7

# 使用square_result作为回调
compute(3, 4, square_result)  # 输出: The squared result is: 49
