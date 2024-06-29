import os

if not os.path.exists('conv_to_stat'): #Pipe lesen, falls vorhanden
    pass
if not os.path.exists('stat_to_report'): #Pipe erstellen, falls noch nicht vorhanden
    os.mkfifo('stat_to_report')

def stat():
    try:
        with open('conv_to_stat', 'r') as pipe_stat, open('stat_to_report', 'a') as log_report: # Pipes öffnen
            values = [] #Array erstellen, um Summe und Mittelwert zu berechnen
            while True:
                value = pipe_stat.readline().strip() # Messwerte aus der Pipe lesen
                if value:
                    values.append(float(value))
                    total = sum(values)
                    total = int(total)
                    mean = total / len(values)
                    mean = int(mean)
                    log_report.write(f"{mean},{total}\n")
                    log_report.flush()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    stat()

