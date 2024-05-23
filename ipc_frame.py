import os
#import posix
import random
import threading

def conv():
    convValues = []
    nr = 6
    for i in range(nr):
        rnd = random.randint(20, 95)
        convValues.append(rnd)
    print(convValues)

conv_thread = threading.Thread(target=conv)
conv_thread.start()
conv_thread.join()
