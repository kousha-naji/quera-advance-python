from threading import Thread
import time

def task_2(i):
    print(f"task {i} : level 1 passed")
    print(f"task {i} :level 2 passed")
    time.sleep(1)
    print(f'task {i} :level 3 passed\n')

threads = [Thread(target=task_2, args=(i,)) for i in range (0, 5)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]