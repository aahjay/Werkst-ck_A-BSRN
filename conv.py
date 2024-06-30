import time
import random
from multiprocessing import shared_memory, Semaphore

def conv():
    # Festlegung der Namen für die Shared Memory Segmente von log und stat
    SHM_NAME_LOG = "shm_log"
    SHM_NAME_STAT = "shm_stat"

    # Erstellung der Shared Memory Segmente und Semaphoren für log und stat
    shm_log = shared_memory.SharedMemory(name=SHM_NAME_LOG, create=True, size=4)
    shm_stat = shared_memory.SharedMemory(name=SHM_NAME_STAT, create=True, size=4)
    # Die Semaphoren bekommen, den Wert 1 als Parameter.
    # Solange der Parameter 1 ist, können Prozesse auf das jeweilige Shared Memory Segment zugreifen
    sem_log = Semaphore(1)
    sem_stat = Semaphore(1)

    try:
        while True:
            # Erwerben der Semaphoren für die Shared Memory Segmente log und stat.
                # Die acquire() Funktion setzt den Parameter der Semaphore auf 0, sodass keine anderen Prozesse
                # auf das Shared Memory Segment zugreifen können
            sem_log.acquire()
            sem_stat.acquire()
            # Generierung der simulierten Werten
            conv_values = random.randint(0, 100)
            # Schreiben der simulierten Werte in die Shared Memory Segmente
                # .buf Funktion der Shared Memory Klasse wird verwendet, um Daten in Shared Memory Bereiche zu schreiben
                # die generierten Zahlen werden in 4 Bytes umgewandelt
                # und befinden sich in den ersten 4 Bytes, des Shared Memory Segmentes
            shm_log.buf[0:4] = conv_values.to_bytes(4, byteorder='little')
            shm_stat.buf[0:4] = conv_values.to_bytes(4, byteorder='little')
            # Freigabe der Semaphoren.
                # release() Funktion setzt den Parameter der Semaphore auf 1 zurück,
                # sodass andere Prozesse auf die Shared Memory Segmente zugreifen können
            sem_log.release()
            sem_stat.release()
                # Simulation einer Pause von 5 Sekunden
            time.sleep(5)
    # Falls Strg-C betätigt wird, werden die Shared Memory Segmente vorerst geschlossen
    # befor sie in der main endgültig gelöscht werden
    except KeyboardInterrupt:
        shm_log.close()
        shm_stat.close()



if __name__ == '__main__':
    conv()
