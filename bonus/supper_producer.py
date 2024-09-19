import asyncio
import random
from aiokafka import AIOKafkaProducer

async def send_random_messages():
    # สร้าง instance ของ AIOKafkaProducer
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092'  # ระบุที่อยู่ของ Kafka broker
    )
    # เริ่ม producer
    await producer.start()
    try:
        while True:
            # สร้างข้อความที่มีค่าเป็นตัวเลขสุ่ม
            random_value = random.randint(0, 100)
            message = f"Random Value: {random_value}".encode('utf-8')

            # ส่งข้อความ
            await producer.send_and_wait("my_topic", message)
            print(f"Sent: {message}")

            # รอ 1 วินาทีก่อนที่จะส่งข้อความถัดไป
            await asyncio.sleep(1)
    finally:
        # ปิด producer
        await producer.stop()

# รันฟังก์ชัน send_random_messages
asyncio.run(send_random_messages())
