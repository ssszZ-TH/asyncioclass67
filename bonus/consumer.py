# https://aiokafka.readthedocs.io/en/stable/

from aiokafka import AIOKafkaConsumer
import asyncio

async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic',
        bootstrap_servers=['192.168.43.194:9096', '192.168.43.113:9096', '192.168.43.11:9096', '192.168.43.147:9096'],  # เชื่อมต่อกับ Kafka brokers หลายตัว
        # group_id="my-group"
        )
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp, msg.headers)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

asyncio.run(consume())