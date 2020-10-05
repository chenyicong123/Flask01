import asyncio
import time

import uvicorn
import aioredis
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()
REDIS_POOL = aioredis.ConnectionsPool('redis://127.0.0.1:6379', minsize=1, maxsize=10)


# @app.get("/")
# def index():
#     """ 普通操作接口 """
#     print("请求来了")
#     time.sleep(3)
#     return {"message": "Hello World"}


@app.get("/red")
async def red():
    """ 异步操作接口 """
    print("请求来了")
    await asyncio.sleep(3)
    async with REDIS_POOL.get() as conn:
        redis = Redis(conn)
        # 设置值
        await redis.hmset_dict('car', key1=1, key2=2, key3=3)
        # 读取值
        result = await redis.hgetall('car', encoding='utf-8')
        print(result)
    return result


if __name__ == '__main__':
    uvicorn.run("10_fastapi:app", host="127.0.0.1", port=5000, log_level="info")
