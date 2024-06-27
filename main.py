import os
import signal
import sys
import time
from multiprocessing import shared_memory

# Dictionary, um Skripte ohne ".py" zu verwenden
scripts = {
    "conv": "conv.py",
    "log": "log.py",
    "stat": "stat.py",
    "report": "report.py"
}

# Liste der gestarteten Kindprozesse
processes = []
# Liste der Namen aller Shared Memory Segmente, die initialisiert werden.
SHM_NAMES = ["shm_log", "shm_stat", "shm_stat_report"]


# Funktion zur Schließung und Auslöschung aller initialisierten Shared Memory Segmente
def cleanup():
    for shm_name in SHM_NAMES:
        shm = shared_memory.SharedMemory(name=shm_name)
        shm.close()
        # unlink() Funktion der Shared Memory Klasse dient zur Auslöschung des Shared Memory Segments
        shm.unlink()

def signal_handler(sig, frame):
    # Beenden aller gestarteten Prozesse
    for pid in processes:
        os.kill(pid, signal.SIGTERM)
    #Aufruf der cleanup() Funktion -> alle Shared Memory Segmente werden geschlossen und zerstört
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
