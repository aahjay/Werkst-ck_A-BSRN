import time
import random
from multiprocessing import shared_memory, Semaphore


def conv():

    # Namen für die Shared Memory Bereiche und Semaphoren für log und stat
    SHM_NAME_LOG = "shm_log"
    SHM_NAME_STAT = "shm_stat"
    SEM_NAME_LOG = "sem_log"
    SEM_NAME_STAT = "sem_stat"

    # Erstellung der Shared Memory Bereiche und Semaphoren für log und stat
    shm_log = shared_memory.SharedMemory(name=SHM_NAME_LOG, create=True, size=4)
    shm_stat = shared_memory.SharedMemory(name=SHM_NAME_STAT, create=True, size=4)
    sem_log = Semaphore(SEM_NAME_LOG, create=True, initial_value=1)
    sem_stat = Semaphore(SEM_NAME_STAT, create=True, initial_value=1)

    while True:
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

