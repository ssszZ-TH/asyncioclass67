import random
import time
import asyncio

class SolarCell:
    def __init__(self, id):
        self.id = id
        self.hardware_readtime = random.randint(1, 3)
        print(f'solar cell {self.id} hardware read time is {self.hardware_readtime}')
        
    async def read_voltage(self):
        voltage = round(random.uniform(3.2, 6.0), 2)
        await asyncio.sleep(self.hardware_readtime)  # แก้ไขให้เป็น await asyncio.sleep
        return voltage
    
async def solarcell_producer(solar_cell, queue1):
    print('solarcell producer: Running')
    while True:
        voltage = await solar_cell.read_voltage()
        await queue1.put(f'solarcell #{solar_cell.id} voltage is {voltage}V timestamp={time.ctime()}')
        await asyncio.sleep(solar_cell.hardware_readtime)

        
async def consumer(queue1):
    print('Consumer: Running')
    while True:
        item = await queue1.get()
        print(f'get msg -> {item}')
        await asyncio.sleep(0.1)
    print('Consumer: Done')

        
async def main():
    num_solar_cells = 5
    queue1 = asyncio.Queue(maxsize=99)
    solar_cells = [SolarCell(i) for i in range(num_solar_cells)]
    
    async with asyncio.TaskGroup() as tg:
        for solar_cell in solar_cells:
            tg.create_task(solarcell_producer(solar_cell, queue1))
        tg.create_task(consumer(queue1))

# รันโปรแกรม
asyncio.run(main())
