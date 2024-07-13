import asyncio
from time import ctime

async def print_time():
    while(True):
        print(ctime())

loop = asyncio.new_event_loop()

task1 = asyncio.sleep(1)

loop.run_until_complete(task1)
loop.close()
print('loop close')