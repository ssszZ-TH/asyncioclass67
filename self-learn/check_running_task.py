import asyncio

async def task_coro():
    print('task running')
    await asyncio.sleep(1)
    print('task done')
    return {'status':500, 'data': 'task done'}

async def main():
    task = asyncio.create_task(task_coro())
    print(f'task.done() = {task.done()}')
    print(f'\nasyncio.current_task() = {asyncio.current_task()}\n')
    await task
    print(f'task.done() = {task.done()}')
    print(f'task.cancelled() = {task.cancelled()}')
    print(f'task.result() = {task.result()}')
    
    # its still pending OMG zombie process !!!
    print(f'\nasyncio.current_task() = {asyncio.current_task()}\n')
    print(f'asyncio.all_tasks() = {asyncio.all_tasks()}')
    
    
    
asyncio.run(main())