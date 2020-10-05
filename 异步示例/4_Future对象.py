import asyncio


async def func(fut):
    # 给Future对象设置结果
    fut.set_result("666")


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 创建一个任务(Future 对象)，这个任务什么都不干
    fut = loop.create_future()
    # 创建一个任务
    await loop.create_task(func(fut))
    # 等待任务最终结果(Future对象)，没有结果则会一直等下去
    data = await fut
    print(data)


asyncio.run(main())
