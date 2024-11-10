import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
    
    def run(self):
        while True:
            print(f"Philosopher {self.index} is thinking")
            time.sleep(random.uniform(0.1, 1))
            print(f"Philosopher {self.index} is hungry")
            self.dine()
    
    def dine(self):
        left, right = self.left_fork, self.right_fork

        with left:
            with right:
                print(f"Philosopher {self.index} is eating")
                time.sleep(random.uniform(0.1, 1))
                print(f"Philosopher {self.index} is done eating")

num_phil = 5
forks = [threading.Lock() for i in range(num_phil)]

philosophers = [
    Philosopher(i, forks[i], forks[(i+1) % num_phil])
    for i in range(num_phil)
]

for philosopher in philosophers:
    philosopher.start()

for phil in philosophers:
    phil.join()