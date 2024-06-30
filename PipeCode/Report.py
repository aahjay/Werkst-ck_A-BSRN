import os
import time

def report():
    try:
        # Öffnen der benannten Pipe im Lesemodus
        with open('stat_to_report', 'r') as stat_report:
            while True:
                # Daten aus der Pipe lesen
                stats = stat_report.readline().strip()
                if stats:
                    mean, total = stats.split(',')
                    print(f"Mean: {mean}, Total: {total}") # Statistische Werte aus der Pipe anzeigen
                    time.sleep(2)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    report()