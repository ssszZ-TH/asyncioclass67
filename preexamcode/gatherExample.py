import asyncio
import time

async def heavy_computation(name, delay):
    """
    Coroutine ที่ทำการประมวลผลหนัก (โดยใช้การ delay แทน).
    
    Args:
        name (str): ชื่อของ task
        delay (int): ระยะเวลาที่จะ delay
    """
    print(f"Task {name}: starting")
    await asyncio.sleep(delay)  # แทนที่การประมวลผลหนักด้วยการ delay
    print(f"Task {name}: finishing after {delay} seconds")

async def main():
    # บันทึกเวลาที่เริ่มต้นการทำงาน
    start_time = time.time()

    # เรียกใช้ coroutines หลายตัวพร้อมกัน
    await asyncio.gather(
        heavy_computation("A", 2),
        heavy_computation("B", 3),
        heavy_computation("C", 1),
    )

    # บันทึกเวลาที่สิ้นสุดการทำงาน
    end_time = time.time()
    print(f"All tasks finished in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    # เรียกใช้ event loop เพื่อรันโปรแกรม
    asyncio.run(main())
