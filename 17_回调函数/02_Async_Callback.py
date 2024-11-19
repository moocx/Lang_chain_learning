""" 
本文件是【回调函数：在 AI 应用中引入异步通信机制】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388071000543346688
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
import asyncio


async def compute(x, y, callback):
    print("Starting compute...")
    await asyncio.sleep(0.5)  # 模拟异步操作
    result = x + y
    # callback(result)
    print("Finished compute...")


def print_result(value):
    print(f"The result is: {value}")


async def another_task():
    print("Starting another task...")
    await asyncio.sleep(1)
    print("Finished another task...")


async def main():
    print("Main starts...")
    task1 = asyncio.create_task(compute(3, 4, print_result))
    task2 = asyncio.create_task(another_task())

    await task1
    await task2
    print("Main ends...")


asyncio.run(main())
