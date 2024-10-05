import asyncio
import random
from aiokafka import AIOKafkaProducer

async def send_random_messages():
    # สร้าง instance ของ AIOKafkaProducer
    producer = AIOKafkaProducer(
        bootstrap_servers=['192.168.43.113:9096', '192.168.43.11:9096', '192.168.43.194:9096', '192.168.43.147:9096']
    )
    # เริ่ม producer
    await producer.start()
    try:
        while True:
            # สร้างข้อความที่มีค่าเป็นตัวเลขสุ่ม
            random_value = random.randint(0, 100)
            message = f"Random Value: {random_value}".encode('utf-8')

            # ส่งข้อความ
            res = await producer.send_and_wait("my_topic", message)
            print(f"Sent: {message}")
            print(f'res=>{res}')

            # รอ 1 วินาทีก่อนที่จะส่งข้อความถัดไป
            await asyncio.sleep(0.5)
    finally:
        # ปิด producer
        await producer.stop()

# รันฟังก์ชัน send_random_messages
asyncio.run(send_random_messages())
