import os

# Benannte Pipe zum Lesen öffnen
if not os.path.exists('conv_to_log'):
    pass

def log():
    try:
        with open('conv_to_log', 'r') as pipe_log, open('log.txt', 'a') as logfile:
            while True:
                # Messwerte aus der Pipe lesen
                value = pipe_log.readline().strip()
                if value:
                    # Messwert in die Logdatei schreiben
                    logfile.write(f"{value}\n")
                    logfile.flush()  # Sicherstellen, dass die Daten sofort geschrieben werden
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    log()

