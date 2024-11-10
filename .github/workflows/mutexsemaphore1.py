import threading
import time
import random

stop_threads = False
buffer = []
buffer_capacity = 5

empty_slots = threading.Semaphore(buffer_capacity)
filled_slots = threading.Semaphore(0)
mutex = threading.Lock()

def producer():
    global stop_threads
    while not stop_threads:
        item = random.randint(1, 100)
        empty_slots.acquire()
        mutex.acquire()

        buffer.append(item)
        print(f"Producer produced {item} | Buffer state: {buffer}")

        mutex.release()
        filled_slots.release()
        time.sleep(random.uniform(0.1, 1))

def consumer():
    global stop_threads
    while not stop_threads:
        filled_slots.acquire()
        mutex.acquire()

        item = buffer.pop(0)
        print(f"Consumer consumed : {item}  | Buffer state : {buffer}")

        mutex.release()
        empty_slots.release()
        time.sleep(random.uniform(0.1, 1))

def timer(duration):
    global stop_threads
    time.sleep(duration)
    stop_threads=True
    print("Timer Stopped")

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
timer_thread =threading.Thread(target=timer, args=(10,))

producer_thread.start()
consumer_thread.start()
timer_thread.start()

producer_thread.join()
consumer_thread.join()
timer_thread.join()