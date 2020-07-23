import _thread
import time

def print_time(tName, delay):
    count = 0;
    while count < 5:
        time.sleep(delay)
        count += 1
        print(tName, time.ctime(time.time()))

try:
    _thread.start_new_thread(print_time,  ("T1", 2, ))
    _thread.start_new_thread(print_time,  ("T2", 4, ))
    pass
except:
    print("Error")
    pass

while 1:
    pass