import time
import asyncio

data1=[5,2,3,1,4]
data2=[50,30,10,20,40]
data3=[500,300,100,200,400]

async def process_data(data, delay):
    print(f'At {time.time()-start_time:.2f} sec, data is {data} delay {delay}')
    asyncio.sleep(delay)
    
    sorted_data = sorted(data)
    print(f'At {time.time()-start_time:.2f} sec, sorted data is {sorted_data}')
    return sorted_data


start_time = time.time()

async def main():
    # sorted_data1 = await process_data(data1, 2)
    # sorted_data2 = await process_data(data2, 3)
    # sorted_data3 = await process_data(data3, 1)
    
    res = await asyncio.gather(process_data(data1, 2), process_data(data2, 3), process_data(data3, 1))

    for i,item in enumerate(res):
        print(f'data {i} sorted is {item}')
    

asyncio.run(main())