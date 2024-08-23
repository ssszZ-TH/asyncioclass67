import time
import asyncio

# เวลาที่ใช้ในการคิดของ Judit (ผู้เล่นหลัก) ต่อหนึ่งการเคลื่อนที่
my_compute_time = 0.1

# เวลาที่ใช้ในการคิดของฝ่ายตรงข้ามต่อหนึ่งการเคลื่อนที่
opponent_compute_time = 0.5

# จำนวนของฝ่ายตรงข้าม
opponents = 24

# จำนวนคู่ของการเคลื่อนที่ที่แต่ละกระดานจะเล่น
move_pairs = 30

async def game(x):
    # เก็บเวลาที่เริ่มต้นการเล่นกระดานนี้
    board_start_time = time.perf_counter()

    # จำลองการเล่นในกระดานนี้
    for i in range(move_pairs):
        # หยุดเวลาเพื่อจำลองการคิดของ Judit ก่อนการเคลื่อนที่
        time.sleep(my_compute_time)
        # พิมพ์ข้อความว่าผู้เล่นหลัก (Judit) ทำการเคลื่อนที่
        print(f'board-{x+1} {i+1} judit make move')
        
        # ฝ่ายตรงข้ามจะคิดและทำการเคลื่อนที่
        # ใช้ asyncio.sleep เพื่อจำลองการคิดของฝ่ายตรงข้ามในระหว่างกระบวนการ async
        if i % 2 == 0:
            await asyncio.sleep(opponent_compute_time)  # เคลื่อนที่ทุกครั้งที่ i เป็นเลขคู่
        else:
            asyncio.sleep(opponent_compute_time + 0.5)  # เคลื่อนที่ทุกครั้งที่ i เป็นเลขคี่

        # พิมพ์ข้อความว่าฝ่ายตรงข้ามทำการเคลื่อนที่
        print(f'board-{x+1} {i+1} opponent make move')

    # พิมพ์ข้อความเมื่อการเล่นในกระดานนี้เสร็จสิ้น พร้อมกับเวลาในการเล่นทั้งหมด
    print(f'board-{x+1} >>>>>>>>>>>> finish move in {time.perf_counter() - board_start_time} seconds')
    
    # คืนค่าเวลาที่ใช้ในการเล่นกระดานนี้ทั้งหมด
    return round(time.perf_counter() - board_start_time)


async def main():
    # สร้างรายการ tasks สำหรับแต่ละกระดาน
    tasks = []
    for i in range(opponents):
        # สร้าง task ที่เป็น coroutine game() และเพิ่มลงในรายการ tasks
        tasks.append(asyncio.create_task(game(i)))

    # รอให้ทุก task ในรายการ tasks ทำงานเสร็จสิ้น
    await asyncio.wait(tasks)

    # พิมพ์เวลาที่ใช้ในการเล่นทั้งหมดของทุกกระดาน
    print(f'board exhibit finish in {time.perf_counter() - start_game} seconds')


if __name__ == "__main__":
    # บันทึกเวลาที่เริ่มต้นการเล่นทั้งหมด
    start_game = time.perf_counter() 
    
    # เรียกใช้ event loop เพื่อรัน main coroutine
    asyncio.run(main())

    # พิมพ์เวลาที่ใช้ทั้งหมดตั้งแต่เริ่มต้นโปรแกรมจนจบ
    print(f'finished in {time.perf_counter() - start_game} seconds')
