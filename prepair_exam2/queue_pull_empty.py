import asyncio
import random
import time

async def main():
    q = asyncio.Queue()
    await q.put(1)  # ไม่ต้องใช้ await
    if not q.empty():
        print(await q.get())  # ไม่ต้องใช้ await

asyncio.run(main())
