# นำเข้าโมดูลที่จำเป็นสำหรับการบันทึกข้อมูล, การใช้ threading และการจัดการเวลา
import logging
import threading
import time 

def thread_function(name):
    # บันทึกข้อมูลเมื่อ thread เริ่มทำงาน
    logging.info("Thread %s: starting", name)
    # หยุดการทำงานของ thread เป็นเวลา 2 วินาที
    time.sleep(2)
    # บันทึกข้อมูลเมื่อ thread ทำงานเสร็จสิ้น
    logging.info("Thread %s: finishing", name)
    
if __name__ == "__main__":
    # กำหนดรูปแบบของข้อความบันทึกข้อมูล
    format = "%(asctime)s: %(message)s"
    # กำหนดการตั้งค่าระบบการบันทึกข้อมูลให้ใช้รูปแบบที่กำหนด และตั้งระดับการบันทึกข้อมูลเป็น INFO
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # บันทึกข้อมูลก่อนที่จะสร้าง thread
    logging.info("Main  : before creating thread")
    # สร้างออบเจ็กต์ thread ใหม่ที่จะเรียกใช้ฟังก์ชัน thread_function พร้อมกับส่งค่าอาร์กิวเมนต์ 1 เข้าไป
    x = threading.Thread(target=thread_function, args=(1,))
    
    # บันทึกข้อมูลก่อนที่จะเริ่ม thread
    logging.info("Main  : before running thread")
    # เริ่มทำงานของ thread
    x.start()
    
    # บันทึกข้อมูลว่ากำลังรอให้ thread ทำงานเสร็จ
    logging.info("Main  : wait for the thread to finish")
    
    # รอให้ thread ทำงานเสร็จ (ในโค้ดนี้ถูกคอมเมนต์ไว้)
    # x.join()
    
    # บันทึกข้อมูลสุดท้ายว่าโปรแกรมหลักทำงานเสร็จแล้ว
    logging.info("Main  : all done")
