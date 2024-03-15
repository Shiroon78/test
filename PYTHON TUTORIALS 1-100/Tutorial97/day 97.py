import threading
import time
from concurrent.futures import ThreadPoolExecutor

# indicate some task
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
    time1 = time.perf_counter()

    # Normal code
    # func(4)
    # func(3)
    # func(1)

    # Some code using thread
    t1 = threading.Thread(target = func, args=[4])
    t2 = threading.Thread(target = func, args=[3])
    t3 = threading.Thread(target = func, args=[1])

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    # Calculating time
    time2 = time.perf_counter()
    print(time2 - time1)

def pullingdemo():
    with ThreadPoolExecutor() as executer:
        # future1 = executer.submit(func, 4)
        # future2 = executer.submit(func, 5)
        # future3 = executer.submit(func, 3)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [1,3,4,7]
        result = executer.map(func, l)
        for results in result:
            print(results)
pullingdemo()