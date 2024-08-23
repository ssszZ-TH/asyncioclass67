from quart import Quart
from quart import render_template

from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

# สร้าง Quart application
app = Quart(__name__)

async def get_pokemon(client, url):
    # แสดงเวลาและ URL ที่กำลังเรียก
    print(f"{time.ctime()} - get {url}")
    # ส่ง GET request แบบ asynchronous ไปยัง URL ที่กำหนด
    resp = await client.get(url)
    # แปลง response เป็น JSON
    pokemon = resp.json()
    return pokemon

async def get_pokemons():
    # สร้าง asynchronous HTTP client
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list = []
        # สร้างรายการตัวเลขสุ่ม 20 ตัว ในช่วง 1-151
        for i in range(20):
            rand_list.append(random.randint(1, 151))
                
        # สร้าง task สำหรับการดึงข้อมูล Pokemon แต่ละตัว
        for number in rand_list:
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.create_task(get_pokemon(client, url)))
            
        # รัน tasks ทั้งหมดพร้อมกันแบบ asynchronous
        pokemon_tasks = await asyncio.gather(*tasks)
        
        # สร้าง Pokemon objects จากข้อมูลที่ได้
        pokemon_data = []
        for pokemon_object in pokemon_tasks:
            pokemon_data.append(Pokemon(pokemon_object))
        
    return pokemon_data

@app.route('/')
async def index():
    # บันทึกเวลาเริ่มต้น
    start_time = time.perf_counter()
    # ดึงข้อมูล Pokemon แบบ asynchronous
    pokemons = await get_pokemons()
    # บันทึกเวลาสิ้นสุด
    end_time = time.perf_counter()
    # แสดงข้อมูลเวลาที่ใช้ในการดึงข้อมูล
    print(f"{time.ctime()} - Get {len(pokemons)} pokemons. Time taken: {end_time - start_time} seconds")
    # แสดงผลหน้า index.html พร้อมส่งข้อมูล Pokemon และเวลา
    return await render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

# รัน Quart app ในโหมด debug ที่ port 50002
if __name__ == '__main__':
    app.run(debug=True, port=50002)