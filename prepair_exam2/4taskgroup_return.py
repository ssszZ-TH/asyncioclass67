import asyncio
import random
import time

async def task_return_rand():
    val = random.randint(1, 10)
    print(val)
    return val

# async def main():
#     rs = []
#     async with asyncio.TaskGroup() as tg:  # ใช้ TaskGroup กับ async with
#         for _ in range(5):
#             r = await tg.create_task(task_return_rand())  # สร้าง task ภายใน TaskGroup
#             rs.append(r)  # นําค่าที่ return มาใส่ใน list
#     print("all tasks done")
#     print(f'rs = {rs}')

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:  # ใช้ TaskGroup กับ async with
        for _ in range(100):
            task = tg.create_task(task_return_rand())  # สร้าง task ภายใน TaskGroup
            tasks.append(task)  # เก็บ task ไว้ใน list
    rs = [task.result() for task in tasks]  # ดึงผลลัพธ์หลังจาก task เสร็จ
    print("all tasks done")
    print(f'rs = {rs}')

start = time.perf_counter()
asyncio.run(main())
print(f'finish in {time.perf_counter() - start:.2f} seconds')
