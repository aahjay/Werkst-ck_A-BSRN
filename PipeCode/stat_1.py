import os

# Benannte Pipe zum Lesen öffnen
if not os.path.exists('conv_to_stat'):
    pass
if not os.path.exists('stat_to_report'):
    os.mkfifo('stat_to_report')

def stat():
    try:
        with open('conv_to_stat', 'r') as pipe_stat, open('stat_to_report', 'a') as log_report:
            values = []
            while True:
                # Messwerte aus der Pipe lesen
                value = pipe_stat.readline().strip()
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



