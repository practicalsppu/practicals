import threading
import time
import random

shared_res = 0
mutex = threading.Lock()
read_count = 0
read_count_mutex = threading.Lock()

write_sem = threading.Semaphore(1)
stop_thread = False

def reader(reader_id):
    global read_count
    while not stop_thread:
        with read_count_mutex:
            read_count += 1
            if read_count == 1:
                write_sem.acquire()
        print(f"Reader {reader_id} is reading shared resource: {shared_res}")
        time.sleep(random.uniform(0.1, 1))

        with read_count_mutex:
            read_count -= 1
            if read_count == 0:
                write_sem.release()
        time.sleep(random.uniform(0.1, 1))

def writer(writer_id):
    while not stop_thread:
        write_sem.acquire()
        with mutex:
            print(f"Writer {writer_id} is writing to shared resource.")
            global shared_res
            shared_res += random.randint(1, 10)
            print(f"Writer {writer_id} has written. New Value : {shared_res}")
        
        write_sem.release()
        time.sleep(random.uniform(0.1, 1))

def timer(duration):
    global stop_thread
    time.sleep(duration)
    stop_thread = True
    print("Timer finished")

num_reader= 5
num_writers = 2
reader_threads = [threading.Thread(target=reader, args=(i+1,)) for i in range(num_reader)]
writer_threads = [threading.Thread(target=writer, args=(i+1,)) for i in range(num_writers)]

for thread in reader_threads + writer_threads:
    thread.start()

timerthread = threading.Thread(target=timer, args=(6,))
timerthread.start()

for thread in reader_threads + writer_threads:
    thread.join()

print("Program has stopped")
