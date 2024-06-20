import time
import random
from multiprocessing import shared_memory
from multiprocessing import get_context

def conv():
    # Festlegung der Namen für die Shared Memory Bereiche und Semaphoren für log und stat
    SHM_NAME_LOG = "shm_log"
    SHM_NAME_STAT = "shm_stat"


    # Erstellung der Shared Memory Bereiche und Semaphoren für log und stat
    shm_log = shared_memory.SharedMemory(name=SHM_NAME_LOG, create=True, size=4)
    shm_stat = shared_memory.SharedMemory(name=SHM_NAME_STAT, create=True, size=4)
    ctx = get_context("spawn")
    sem_log = ctx.Semaphore(1)
    sem_stat = ctx.Semaphore(1)


    while True:
        # Erwerben der Semaphoren für die Shared Memory Bereiche log und stat
        sem_log.acquire()
        sem_stat.acquire()
        # Generierung und Ausgabe von simulierten Werten
        conv_values = random.randint(0, 100)
        print(conv_values)
        # Schreiben der simulierten Werte in die Shared Memory Bereiche
        shm_log.buf[0:4] = conv_values.to_bytes(4, byteorder='little')
        shm_stat.buf[0:4] = conv_values.to_bytes(4, byteorder='little')
        # Freigabe der Semaphoren
        sem_log.release()
        sem_stat.release()
        time.sleep(5)


if __name__ == '__main__':
    conv()
