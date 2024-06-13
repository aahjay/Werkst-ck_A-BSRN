import os
import signal
import sys

# Pfade zu den einzelnen Skripten
scripts = {
    "conv": "conv.py",
    "log": "log.py",
    "stat": "stat.py",
    "report": "report.py"
}

# Liste der gestarteten Kindprozesse
processes = []

def fork_and_exec(script):
    pid = os.fork()
    if pid == 0:
        # Kindprozess: Ersetze den Prozess durch das jeweilige Skript (Übergabeparameter d. Funktion)
        os.execlp(sys.executable, sys.executable, script)
    else:
        # Elternprozess: Rückgabe der PID des Kindprozesses
        return pid

try:
    # Starten der einzelnen Prozesse
    for name, script in scripts.items():
        pid = fork_and_exec(script)
        processes.append(pid)

except Exception as e:
    print("Fehler beim Starten der Prozesse:  {e}")