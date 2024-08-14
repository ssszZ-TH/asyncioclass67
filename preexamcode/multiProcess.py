import multiprocessing
import time
import os

'''
ในการใช้งานจริง อาจจะต้องเปลีย่น code จากการ forloop นรกเป็น delay เเทน เพราะว่าเครื่องผมเร็วเกินไป 

'''

def heavy_computation(name):
    print(f"Process {name}: starting with PID {os.getpid()}")
    total = 0
    for i in range(1000000):
        total += i
    print(f"Process {name}: finishing with total = {total} and PID {os.getpid()}")

if __name__ == "__main__":
    start_time = time.time()

    # สร้าง process สองตัวเพื่อทำงานหนัก
    processes = []
    for i in range(2):
        process = multiprocessing.Process(target=heavy_computation, args=(i,))
        processes.append(process)
        process.start()

    # รอให้ทุก process ทำงานเสร็จ
    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Multiprocessing took {end_time - start_time:.2f} seconds")
