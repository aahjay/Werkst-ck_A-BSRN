from multiprocessing import shared_memory, Semaphore

def report():

    # Festlegung der Namen für den Shared Memory Bereich und die Semaphore von stat und report
    SHM_NAME_STAT_REPORT = "shm_stat_report"
    SEM_NAME_STAT_REPORT = "sem_stat_report"
    # Öffnen des bereits existierenden Shared Memory Bereiches von stat und report
    shm_stat_report = shared_memory.SharedMemory(name=SHM_NAME_STAT_REPORT)
    sem_stat_report = Semaphore(SEM_NAME_STAT_REPORT)


    while True:
        # Erwerben der Semaphore für den Shared Memory Bereich stat_report
        sem_stat_report.acquire()
        # Lesen der in stat berechneten Datem aus dem Shared Memory Bereich
        total = int.from_bytes(shm_stat_report.buf[0:4], 'little')
        mean = int.from_bytes(shm_stat_report.buf[4:8], 'little')
        # Freigabe der Semaphore
        sem_stat_report.release()
        # Ausgabe der in stat errechneten Werte
        print(f"Mean: {mean}, Total: {total}")
