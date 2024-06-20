import os
import signal
import sys
import time
from multiprocessing import shared_memory

# Pfade zu den einzelnen Skripten
scripts = {
    "conv": "conv.py",
    "log": "log.py",
    "stat": "stat.py",
    "report": "report.py"
}

# Liste der gestarteten Kindprozesse
processes = []

SHM_NAMES = ["shm_log", "shm_stat", "shm_stat_report"]
SEM_NAMES = ["sem_log", "sem_stat", "sem_stat_report"]


def cleanup(): # Funktion zur Schließung und Freigabe aller initialisierten Shared Memory Segmente
    for shm_name in SHM_NAMES:
        shm = shared_memory.SharedMemory(name=shm_name)
        shm.close()
        shm.unlink()

def signal_handler(sig, frame):
    # Beenden aller gestarteten Prozesse
    for pid in processes:
        os.kill(pid, signal.SIGTERM)
    cleanup()
    print("cleaning up...")
    sys.exit(0)

# Setzen des Signal-Handlers für SIGINT
signal.signal(signal.SIGINT, signal_handler)
    
def fork_and_exec(script):
    pid = os.fork()
    if pid == 0:
        # Kindprozess: Ersetzen des Prozess durch das jeweilige Skript (Übergabeparameter d. Funktion)
        os.execlp(sys.executable, sys.executable, script)
    else:
        # Elternprozess: Rückgabe der PID des Kindprozesses
        return pid

try:
    # Starten der einzelnen Prozesse
    for name, script in scripts.items():
        pid = fork_and_exec(script)
        print(f"{name} started")
        time.sleep(2)
        processes.append(pid)
        
    for pid in processes:
        os.waitpid(pid, 0)

    cleanup()

    # Abfangen von Fehlern bei der Ausführung
except Exception as e:
    print("Fehler beim Starten der Prozesse:  {e}")
    signal_handler(None, None)
