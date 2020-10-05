import asyncio


async def fun1():
    print(1)
    await asyncio.sleep(1)
    print(2)
    return 3


async def main():
    print("main开始")
    task_list = [
        asyncio.create_task(fun1()),
        asyncio.create_task(fun1()),
    ]
    print("main结束")
    # done 为完成的结果集，pending 为未完成的结果集
    done, pending = await asyncio.wait(task_list, timeout=10)


if __name__ == '__main__':
    asyncio.run(main())
