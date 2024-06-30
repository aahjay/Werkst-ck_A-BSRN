import time
from multiprocessing import shared_memory, Semaphore


def log():
    # Festlegung des Namen für das Shared Memory Segment von conv und log
    SHM_NAME_LOG = "shm_log"
    # Öffnen des Shared Memory Segmentes von conv und log
    shm_log = shared_memory.SharedMemory(name=SHM_NAME_LOG)
    sem_log = Semaphore(1)

    # Öffnet eine neue log-Datei (Textdokument) bzw. die bereits im Verzeichnis existierende log-Datei
    try:
        with open('log.txt', 'a') as file:
            while True:
                # Erwerben der Semaphore für das Shared Memory Segment log
                sem_log.acquire()
                # Lesen der Werte aus dem Shared Memory Segment.
                    # Die ersten 4 Bytes des shm_log werden in einen Integer umgewandelt und in der Variable gespeichert
                conv_value = int.from_bytes(shm_log.buf[0:4], byteorder='little')
                # Freigabe der Semaphore
                sem_log.release()
                # Schreiben der empfangenen Werte aus dem Shared Memory Segment in die Datei 'log.txt'
                file.write(f"{conv_value}\n")
                file.flush()
                time.sleep(5)
    except KeyboardInterrupt:
        shm_log.close()

if __name__ == '__main__':
    log()