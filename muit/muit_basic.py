from ntpath import join
import time 
import threading

start = time.perf_counter()

def do_something():
    print("sleeping 1 second__")
    time.sleep(1)
    print ("done sleeping" )

t2 = threading.Thread(target=do_something)

t1 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()

t2.join()


finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} second(s)')