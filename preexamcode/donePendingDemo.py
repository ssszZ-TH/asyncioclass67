import asyncio
import random

async def task_with_random_delay(task_id):
    delay = random.uniform(1, 5)
    print(f"Task {task_id} starting, will take {delay:.2f} seconds")
    await asyncio.sleep(delay)
    print(f"Task {task_id} completed after {delay:.2f} seconds")
    return f"Result from Task {task_id}"

async def main():
    # สร้าง tasks จำนวน 10 อัน
    tasks = [asyncio.create_task(task_with_random_delay(i)) for i in range(10)]

    # รอ tasks โดยใช้ timeout 3 วินาที
    print("Waiting for tasks to complete (with 3 second timeout)...")
    done, pending = await asyncio.wait(tasks, timeout=3)

    print(f"\n{len(done)} tasks completed:")
    for task in done:
        result = await task
        print(f"- {result}")

    print(f"\n{len(pending)} tasks still pending:")
    for task in pending:
        print(f"- Task {tasks.index(task)} is still running")

    # ยกเลิก tasks ที่ยังค้างอยู่
    for task in pending:
        task.cancel()

    # รอให้ tasks ที่ถูกยกเลิกเสร็จสิ้น
    await asyncio.gather(*pending, return_exceptions=True)

    print("\nAll tasks have been completed or cancelled")

if __name__ == "__main__":
    asyncio.run(main())