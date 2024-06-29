import os
import signal
import sys

# dictionary für die Prozess-Skripte
scripts = {
    "conv": "PipeCode/conv.py",
    "log": "PipeCode/log.py",
    "stat": "PipeCode/stat_1.py",
    "report": "PipeCode/report.py"
}

# Liste der gestarteten Kindprozesse
processes = []

def signal_handler(sig, frame):
    # Beenden aller gestarteten Prozesse
    for pid in processes:
        try:
            print('\nterminating process: ' + str(pid))
            os.kill(pid, signal.SIGTERM)
        except OSError:
            pass
    sys.exit(0)

 # Signal-Handler für SIGINT
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
        print (f'Starting {name} process...\n')
        processes.append(pid)
        
    for pid in processes:
        os.waitpid(pid, 0)

    # Abfangen von Fehlern bei der Ausführung
except Exception as e:
    print("-- Fehler beim Starten der Prozesse --")
    signal_handler(None, None)