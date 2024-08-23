import asyncio
import aiohttp
import time

urls = [
    'https://pokeapi.co/api/v2/ability/battle-armor',
    'https://pokeapi.co/api/v2/ability/speed-boost'
]

async def fetch(session, url):
    start_time = time.time()
    async with session.get(url) as response:
        end_time = time.time()
        print(f'async get : {url} time taken : {end_time - start_time}')
        return await response.json()
    

async def main():
    start_time = time.time()  # เริ่มจับเวลา

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        for url, result in zip(urls, results):
            print(f"Data from {url}:")
            pokemon_names = result['pokemon']
            counter = 0
            for pokemon in pokemon_names:
                print(pokemon['pokemon']['name'],end=', ')
                counter += 1
                
            print(f"\nTotal number of pokemons: {counter}")

            print("\n---------------------------------------\n")

    end_time = time.time()  # จบการจับเวลา
    total_time = end_time - start_time
    print(f"Total execution time: {total_time:.10f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
