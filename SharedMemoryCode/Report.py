from multiprocessing import shared_memory, Semaphore
import time

def report():

    # Festlegung der Namen für das Shared Memory Segment und die Semaphore von stat und report
    SHM_NAME_STAT_REPORT = "shm_stat_report"
    # Öffnen des bereits existierenden Shared Memory Segments von stat und report
    shm_stat_report = shared_memory.SharedMemory(name=SHM_NAME_STAT_REPORT)
    sem_stat_report = Semaphore(1)

    try:
        while True:
            # Erwerben der Semaphore für das Shared Memory Segment stat_report
            sem_stat_report.acquire()
            # Lesen der in stat berechneten Daten aus dem Shared Memory Segment
            print("fetching mean and total from shm_stat_report")
            total = int.from_bytes(shm_stat_report.buf[0:4], 'little')
            mean = int.from_bytes(shm_stat_report.buf[4:8], 'little')
            # Freigabe der Semaphore
            sem_stat_report.release()
            # Ausgabe der in stat errechneten Werte
            print(f"Mean: {mean}, Total: {total}")
            time.sleep(5)
    except KeyboardInterrupt:
        shm_stat_report.close()

if __name__ == "__main__":
    report()