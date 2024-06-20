from multiprocessing import shared_memory, get_context
import time

def log():
    # Festlegung der Namen für den Shared Memory Bereich und der Semaphore von conv und log
    SHM_NAME_LOG = "shm_log"

    # Öffnen des Shared Memory Bereiches von conv und log
    shm_log = shared_memory.SharedMemory(name=SHM_NAME_LOG)
    ctx = get_context("spawn")
    sem_log = ctx.Semaphore(1)

    # Öffnet eine neue log-Datei (Textdokument) bzw. die bereits im Verzeichnis existierende log-Datei
    with open('log.txt', 'a') as file:
        while True:
            # Erwerben der Semaphore für den Shared Memory Bereich log
            sem_log.acquire()
            # Lesen der Werte aus dem Shared Memory Bereich
            conv_value = int.from_bytes(shm_log.buf[0:4], byteorder='little')
            print("fetching data from shm_log")
            # Freigabe der Semaphore
            sem_log.release()
            # Schreiben der empfangenen Werte aus dem Shared Memory Bereich in die Datei 'log.txt'
            file.write(f"{conv_value}\n")
            file.flush()
            time.sleep(5)

if __name__ == '__main__':
    log()