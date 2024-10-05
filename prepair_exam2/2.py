import time
import asyncio
import math

picases = [
    [6,9],
    [2,8],
    [3,7],
    [4,6],
    [3,5],
    [7,4],
    [5,3],
    [1,2],
    [8,2],
    [6,1],
]

async def calc_distance(x2, y2, x1=3, y1=3):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


async def main():
     # create many coroutines
    coros = [calc_distance(picas[0], picas[1]) for picas in picases]
    # run the tasks
    res = await asyncio.gather(*coros)
    for i, item in enumerate(res):
        print(f'anthena {i} picas {picases[i]} distance is {item}')
        
    print(f'min={min(res)} max={max(res)} mean={sum(res)/len(res)} stdev={math.sqrt(sum((x - sum(res) / len(res)) ** 2 for x in res) / len(res))}')
    print(f'min_point={res.count(min(res))} max_point={res.count(max(res))}')
    nearest_anthena = [i for i in range(len(res)) if res[i] in [min(res)]]
    fartest_anthena = [i for i in range(len(res)) if res[i] in [max(res)]]
    for _ in nearest_anthena:
        print(f'nearest anthena is {picases[_]}')
    for _ in fartest_anthena:
        print(f'fartest anthena is {picases[_]}')
    
asyncio.run(main())