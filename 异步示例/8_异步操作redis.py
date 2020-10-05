import asyncio
import aioredis


async def execute(address):
    print("开始执行", address)
    # 连接redis
    redis = await aioredis.create_redis_pool(address)
    # 网络IO操作：遇到IO会自动切换任务
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)
    # 网络IO操作：遇到IO会自动切换任务
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)
    redis.close()
    # 网络IO操作：遇到IO会自动切换任务
    await redis.wait_closed()
    print("结束", address)


task_list = [
    execute('redis://127.0.0.1:6379'),
    execute('redis://127.0.0.1:6379'),
]
asyncio.run(asyncio.wait(task_list))
