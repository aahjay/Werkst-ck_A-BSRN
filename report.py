from multiprocessing import shared_memory, Semaphore

def report():
    SHM_NAME_STAT_REPORT = "shm_stat_report"
    SEM_NAME_STAT_REPORT = "sem_stat_report"

    shm_stat_report = shared_memory.SharedMemory(name=SHM_NAME_STAT_REPORT)
    sem_stat_report = Semaphore(SEM_NAME_STAT_REPORT)


    while True:
        sem_stat_report.acquire()
        total = int.from_bytes(shm_stat_report.buf[0:4], 'little')
        mean = int.from_bytes(shm_stat_report.buf[4:8], 'little')
        sem_stat_report.release()
        print(f"Mean: {mean}, Total: {total}")
