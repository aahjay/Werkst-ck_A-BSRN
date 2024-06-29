import os
import random
import time

if not os.path.exists('conv_to_log'): #Pipe erstellen, falls noch nicht vorhanden
    os.mkfifo('conv_to_log')
if not os.path.exists('conv_to_stat'): #Pipe erstellen, falls noch nicht vorhanden
    os.mkfifo('conv_to_stat')

def conv():
    try:
        with open('conv_to_log', 'a') as conv_to_log, open('conv_to_stat', 'a') as conv_to_stat: #Pipes öffnen
            while True:
                value = random.randint(1, 100) #Random Integer erstellen
                conv_to_log.write(f"{value}\n")
                conv_to_log.flush() #Sicherstellen, dass Zahlen sofort in Datei geschrieben werden
                conv_to_stat.write(f"{value}\n")
                conv_to_stat.flush()
                time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    conv()

