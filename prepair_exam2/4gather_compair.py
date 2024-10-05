import asyncio
import random
import time

# จาก code เมื่อกี้ เอามาเทียบกับ gather ก็จะทำงานเหมือนกัน

async def task_return_rand():
    val = random.randint(1, 10)
    print(val)
    return val

async def main():
    tasks = [task_return_rand() for _ in range(5)]
    rs = await asyncio.gather(*tasks)
    print("all tasks done")
    print(f'rs = {rs}')


start = time.perf_counter()
asyncio.run(main())
print(f'finish in {time.perf_counter() - start:.2f} seconds')
