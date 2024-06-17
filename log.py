from multiprocessing import shared_memory, Semaphore


def log():
    SHM_NAME_LOG = "shm_log"
    SEM_NAME_LOG = "sem_log"

    shm_log = shared_memory.SharedMemory(name=SHM_NAME_LOG)
    sem_log = Semaphore(name=SEM_NAME_LOG)

    # öffnet eine neue log-Datei (Textdokument) bzw. die bereits im Verzeichnis existierende log-Datei
    with open('log.txt', 'a') as file:
        while True:
            sem_log.acquire()
            conv_values = int.from_bytes(shm_log.buf[0:4], byteorder='little')
            sem_log.release()
        # schreibt die Werte aus conv in die Datei 'log.txt'
            file.write(f"{conv_values}\n")
