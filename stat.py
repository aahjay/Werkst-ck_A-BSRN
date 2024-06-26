import time
from multiprocessing import shared_memory, Semaphore

def stat():
    # Festlegung der Namen für die Shared Memory Segmente und Semaphoren für stat und report
    SHM_NAME_STAT = "shm_stat"
    SHM_NAME_STAT_REPORT = "shm_stat_report"

    # Öffnen des bereits existierenden Shared Memory Segmentes stat
    shm_stat = shared_memory.SharedMemory(name=SHM_NAME_STAT)
    sem_stat = Semaphore(1)
    # Initialisierung eines neuen Shared Memory Segmentes mit Semaphore zur Speicherung der Berechnungen aus stat für den report Prozess
    shm_stat_report = shared_memory.SharedMemory(name=SHM_NAME_STAT_REPORT, create=True, size=8)
    sem_stat_report = Semaphore(1)

    conv_values = []   # Initialisierung einer leere Liste, um die empfangenen Werte zu speichern

    # Funktion, welche die Summe und den Mittelwert der aus conv generierten Werte berechnet
    def calculate_stats():
        total = sum(conv_values)
        count = len(conv_values)
        mean = total // count
        return mean, total

    try:
        while True:
            # Erwerben der Semaphore für den Shared Memory Bereich stat
            sem_stat.acquire()
            # Lesen der generierten Werte aus dem Shared Memory Bereich
            print("fetching data from shm_stat")
            conv_value = int.from_bytes(shm_stat.buf[0:4], byteorder='little')
            # Hinzufügen der eingelesenen Werte zur zuvor erstellten conv_values Liste
            print(f"adding value {conv_value} to list")
            conv_values.append(conv_value)
            # Freigabe der Semaphore
            sem_stat.release()
            print("calculating stats")
            mean, total = calculate_stats()
            # Erwerben der Semaphore für das Shared Memory Segment von stat und report
            sem_stat_report.acquire()
            # Übergabe der Berechneten Werte in den Shared Memory Segment von stat und report
            print("sending mean and total to shm_stat_report")
            shm_stat_report.buf[0:4] = total.to_bytes(4, byteorder='little')
            shm_stat_report.buf[4:8] = mean.to_bytes(4, byteorder='little')
            # Freigabe der Semaphore
            sem_stat_report.release()
            time.sleep(5)
    except KeyboardInterrupt:
        shm_stat.close()
        shm_stat_report.close()


if __name__ == '__main__':
    stat()
