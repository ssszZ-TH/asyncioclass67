from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(food):
    # generate a random value between 0 and 1
    waitfor = 1 + random()
    
    print(f'microwave ({food}): cooking for {waitfor} seconds') ## always print
    await asyncio.sleep(waitfor)
    print(f'microwave ({food}) finish cooking') ## print when complete firstly
    

    return f'{food} is complete in {waitfor} seconds'

# main coroutine
async def main():
    # create many tasks
    tasks = [
        asyncio.create_task(task_coro('rice')),
        asyncio.create_task(task_coro('noodle')),
        asyncio.create_task(task_coro('curry'))
    ]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, timeout=10, return_when=asyncio.FIRST_COMPLETED)

    # get the result of the first completed task
    first_completed_task = done.pop()
    print('First completed task result:')
    print(first_completed_task.result())

    print(f'Number of tasks still pending: {len(pending)}')
    # for task in pending:
    #     print(f'Pending task: {task}')

asyncio.run(main())
