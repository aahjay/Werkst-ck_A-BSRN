import threading
from multiprocessing import shared_memory, Semaphore


def log():
    SHM_NAME_LOG = "shm_log"
    SEM_NAME_LOG = "sem_log"

    shm_log = shared_memory.SharedMemory(name=SHM_NAME_LOG)
    sem_log = Semaphore(name=SEM_NAME_LOG)

    # öffnet eine neue log-Datei (Textdokument) bzw. die bereits im Verzeichnis existierende log-Datei
    with open('log.txt', 'a') as file:
        # schreibt die Werte aus conv in die Datei 'log.txt'
        file.write(conv_values + ' \n')