import os

def report():
    try:
        # Öffnen der benannten Pipe im Lesemodus
        with open('stat_to_report', 'r') as stat_report:
            while True:
                # Daten aus der Pipe lesen
                stats = stat_report.readline().strip()
                if stats:
                    mean, total = stats.split(',')
                    print(f"Mittelwert: {mean}, Summe: {total}") # Statistische Werte aus der Pipe anzeigen
    except KeyboardInterrupt:
        pass






