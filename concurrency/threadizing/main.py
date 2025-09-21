import functions
from threading import Thread

def threadize() -> None:
    def run_thread_with_funcs(function_list):
        threads = []
        for i, func in enumerate(function_list):
            t = Thread(target=func, name=str(i+1))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    run_thread_with_funcs(functions.f)
    run_thread_with_funcs(functions.g)
    run_thread_with_funcs(functions.h)



    # thread_1 = Thread(name='1', target=functions.f[0])
    # thread_2 = Thread(name='2', target=functions.f[1])
    # thread_3 = Thread(name='3', target=functions.f[2])
    # thread_4 = Thread(name='4', target=functions.f[3])

    # thread_1.start()
    # thread_2.start()
    # thread_3.start()
    # thread_4.start()

    # thread_1.join()
    # thread_2.join()
    # thread_3.join()
    # thread_4.join()
    
    # thread_1 = Thread(name='1', target=functions.g[0])
    # thread_2 = Thread(name='2', target=functions.g[1])
    
    # thread_1.start()
    # thread_2.start()
    
    # thread_1.join()
    # thread_2.join()
    
    # thread_1 = Thread(name='1', target=functions._h[0])
    
    # thread_1.start()
    
    # thread_2.join()