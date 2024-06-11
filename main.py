import os
import signal
import sys

# Pfade zu den einzelnen Skripten
scripts = {
    "conv": "Conv.py",
    "log": "Log.py",
    "stat": "Stat.py",
    "report": "Report.py"
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