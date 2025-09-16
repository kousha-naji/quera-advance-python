import time
import threading
from threading import Thread

# def f():
#     print(f"The thread \"{threading.current_thread().name}\" started.")
#     time.sleep(1)
#     print(f"The thread \"{threading.current_thread().name}\" finished.")

# t = Thread(name='hello', target=f)

# # t.daemon = True

# t.start()

# time.sleep(0.1)
# for i in range(5):
#     print(i)




# def f():
#     print(f"The thread \"{threading.current_thread().name}\" started.")
#     time.sleep(1)
#     print(f"The thread \"{threading.current_thread().name}\" finished.")

# t = Thread(name='hello', target=f)

# t.daemon = True

# t.start()

# time.sleep(0.1)
# for i in range(5):
#     print(i)


def f(i):
    print(f"[{threading.current_thread().name}] is starting.")
    time.sleep(i)
    print(f"[{threading.current_thread().name}] is finishing.")

ls = []
for i in range(1, 5):
    ls.append(Thread(name=f"t{str(i)}", target=f, args=(i,)))

for t in ls:
    t.start()

time.sleep(3)

for t in threading.enumerate():
    print(f"[{t.name}] is alive now!")