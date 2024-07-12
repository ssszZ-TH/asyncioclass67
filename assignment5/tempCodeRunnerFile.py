from random import random
import asyncio
from time import sleep

# coroutine to execute in a new task
async def task_coro(food):
    # generate a random value between 0 and 1
    waitfor = 1 + random()
    # block for a moment
    asyncio.sleep(waitfor)
    # report the value
    print(f'microwave ({food}): cooking for {waitfor} seconds')
    return f'microwave ({food}): cooking for {waitfor} seconds'
# main coroutine
async def main():
    # create many tasks
    tasks = [
        asyncio.create_task(task_coro('rice')),
        asyncio.create_task(task_coro('noodle')),
        asyncio.create_task(task_coro('curry'))
    ]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, timeout=10 , return_when=asyncio.FIRST_COMPLETED)
    print('first complete')
    print(done.pop().result())

asyncio.run(main())
