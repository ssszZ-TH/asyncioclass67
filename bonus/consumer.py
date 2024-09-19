# https://aiokafka.readthedocs.io/en/stable/

import asyncio
from aiokafka import AIOKafkaConsumer

async def consume():
    # สร้าง instance ของ AIOKafkaConsumer
    consumer = AIOKafkaConsumer(
        'my_topic',
        bootstrap_servers='localhost:9093',
        group_id="my-group"
    )
    # เริ่ม consumer
    await consumer.start()
    try:
        # อ่านข้อความ
        async for msg in consumer:
            print(f"Consumed message: {msg.value.decode('utf-8')}")
    finally:
        # ปิด consumer
        await consumer.stop()

# รันฟังก์ชัน consume
asyncio.run(consume())
