# import asyncio

# async def febonaccci(n):
#     await asyncio.sleep(1)
#     a,b = 0,1
#     if n<=1:
#         return n
#     else :
#         for i in range(1,n):
#             c = a+b
#             a=b
#             b=c
#         return b
# async def main():
#     n=10
#     coros = [asyncio.create_task(febonaccci(i)) for i in range(n)]
#     resault = await asyncio.gather(*coros)
    
#     print(resault)
    
# asyncio.run(main())

import asyncio

async def fibonacci(n):
    await asyncio.sleep(1)
    a, b = 0, 1
    if n <= 1:
        return n
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

async def main():
    n = 10
    tasks = [asyncio.create_task(fibonacci(i)) for i in range(n)]
    
    # ใช้ asyncio.wait แทน asyncio.gather
    done, _ = await asyncio.wait(tasks)
    
    # เรียงลำดับผลลัพธ์ตาม task ที่สร้าง
    # result = [t.result() for t in sorted(done, key=lambda t: tasks.index(t))]
    result = [t.result() for t in done]
    
    print(result)

asyncio.run(main())
