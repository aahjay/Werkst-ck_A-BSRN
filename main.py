import os
import signal
import sys
import time

# Pfade zu den einzelnen Skripten
scripts = {
    "conv": "conv.py",
    "log": "log.py",
    "stat": "stat.py",
    "report": "report.py"
}

# Liste der gestarteten Kindprozesse
processes = []

def signal_handler(sig, frame):
    # Beenden Sie alle gestarteten Prozesse
    for pid in processes:
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError:
            pass
    sys.exit(0)

 # Setzen Sie den Signal-Handler für SIGINT
signal.signal(signal.SIGINT, signal_handler)
    
def fork_and_exec(script):
    pid = os.fork()
    if pid == 0:
        # Kindprozess: Ersetzen des Prozesses durch das jeweilige Skript (Übergabeparameter d. Funktion)
        os.execlp(sys.executable, sys.executable, script)
    else:
        # Elternprozess: Rückgabe der PID des Kindprozesses
        return pid

try:
    # Starten der einzelnen Prozesse
    for name, script in scripts.items():
        pid = fork_and_exec(script)
        time.sleep(2)
        print(f"Starting {name} process...")
        processes.append(pid)
        
    for pid in processes:
        os.waitpid(pid, 0)

    # Abfangen von Fehlern bei der Ausführung
except Exception as e:
    print("Fehler beim Starten der Prozesse:  {e}")
    signal_handler(None, None)
