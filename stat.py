from multiprocessing import shared_memory, Semaphore

def stat():
    # Festlegung der Namen für die Shared Memory Bereiche und Semaphoren für stat und report
    SHM_NAME_STAT = "shm_stat"
    SHM_NAME_STAT_REPORT = "shm_stat_report"
    SEM_NAME_STAT = "sem_stat"
    SEM_NAME_STAT_REPORT = "sem_stat_report"

    # Öffnen des bereits existierenden Shared Memory Bereiches stat
    shm_stat = shared_memory.SharedMemory(name=SHM_NAME_STAT)
    sem_stat = Semaphore(SEM_NAME_STAT)
    # Initialisierung eines neuen Shared Memory Bereiches mit Semaphore zur Speicherung der Berechnungen aus stat für report
    shm_stat_report = shared_memory.SharedMemory(name=SHM_NAME_STAT_REPORT, create=True, size=8)
    sem_stat_report = Semaphore(SEM_NAME_STAT_REPORT, create=True, initial_value=1)

    conv_values = []   # Initialisierung einer leere Liste, um die empfangenen Werte zu speichern

    # Funktion, welche die Summe und den Mittelwert der aus conv generierten Werte berechnet
    def calculate_stats():
        total = sum(conv_values)
        mean = total / len(conv_values)
        return mean, total

    while True:
        # Erwerben der Semaphore für den Shared Memory Bereich stat
        sem_stat.acquire()
        # Lesen der generierten Werte aus dem Shared Memory Bereich
        conv_value = int.from_bytes(shm_stat.buf[0:4], byteorder='little')
        # Hinzufügen der eingelesenen Werte zur zuvor erstellten conv_values Liste
        conv_values.append(conv_value)
        # Freigabe der Semaphore
        sem_stat.release()
        total, mean = calculate_stats()
        # Erwerben der Semaphore für den Shared Memory Bereich von stat und report
        sem_stat_report.acquire()
        # Übergabe der Berechneten Werte in den Shared Memory Bereich von stat und report
        shm_stat_report.buf[0:4] = int(total).to_bytes(4, byteorder='little')
        shm_stat_report.buf[0:4] = int(mean).to_bytes(4, byteorder='little')
        # Freigabe der Semaphore
        sem_stat_report.release()
