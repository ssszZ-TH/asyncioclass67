import threading
import time
import os

def heavy_computation(name):
    print(f"Thread {name}: starting with PID {os.getpid()}")
    total = 0
    for i in range(1000000):
        total += i
    print(f"Thread {name}: finishing with total = {total} and PID {os.getpid()}")

if __name__ == "__main__":
    start_time = time.time()

    # สร้าง thread สองตัวเพื่อทำงานหนัก
    threads = []
    for i in range(2):
        thread = threading.Thread(target=heavy_computation, args=(i,))
        threads.append(thread)
        thread.start()

    # รอให้ทุก thread ทำงานเสร็จ
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Multithreading took {end_time - start_time:.2f} seconds")
