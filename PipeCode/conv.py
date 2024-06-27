import os
import random
import time

if not os.path.exists('conv_to_log'):
    os.mkfifo('conv_to_log')
if not os.path.exists('conv_to_stat'):
    os.mkfifo('conv_to_stat')

def conv():
    try:
        with open('conv_to_log', 'a') as conv_to_log, open('conv_to_stat', 'a') as conv_to_stat:
            while True:
                value = random.randint(1, 100)
                conv_to_log.write(f"{value}\n")
                conv_to_log.flush()
                conv_to_stat.write(f"{value}\n")
                conv_to_stat.flush()
                time.sleep(1)
    except KeyboardInterrupt:
        pass

