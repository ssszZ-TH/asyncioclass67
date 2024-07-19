import asyncio
from time import time


async def coro1():
    print(f'coro1 started {(time()-startTime) * 1000} ms')
    await asyncio.sleep(1)
    print(f'coro1 stopped {(time()-startTime) * 1000} ms')
    return 1

async def coro2():
    print(f'coro2 started {(time()-startTime) * 1000} ms')
    print(f'coro2 stopped {(time()-startTime) * 1000} ms')
    return 2

async def poison():
    raise Exception('poisoned')
    
async def main():
    
    
    
    results = await asyncio.gather(coro1(), coro2(), return_exceptions=True)
    print(f'results = {results}')
    
    results = await asyncio.gather(coro1(), poison(), return_exceptions=True)
    print(f'results = {results}')
    

startTime = time()
asyncio.run(main())
    