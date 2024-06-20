from multiprocessing import shared_memory, Semaphore, get_context#
import time

def report():

    # Festlegung der Namen für den Shared Memory Bereich und die Semaphore von stat und report
    SHM_NAME_STAT_REPORT = "shm_stat_report"
    ctx = get_context("spawn")
    # Öffnen des bereits existierenden Shared Memory Bereiches von stat und report
    shm_stat_report = shared_memory.SharedMemory(name=SHM_NAME_STAT_REPORT)
    sem_stat_report = ctx.Semaphore(1)


    while True:
        # Erwerben der Semaphore für den Shared Memory Bereich stat_report
        sem_stat_report.acquire()
        # Lesen der in stat berechneten Datem aus dem Shared Memory Bereich
        print("fetching mean and total from shm_stat_report")
        total = int.from_bytes(shm_stat_report.buf[0:4], 'little')
        mean = int.from_bytes(shm_stat_report.buf[4:8], 'little')
        # Freigabe der Semaphore
        sem_stat_report.release()
        # Ausgabe der in stat errechneten Werte
        print(f"Mean: {mean}, Total: {total}")
        time.sleep(5)

if __name__ == "__main__":
    report()
