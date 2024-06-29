import time
import posix_ipc
import struct

def log():
    mq_conv_log = posix_ipc.MessageQueue("/mq_conv_log") #Auf Message Queue zugreifen

    try:
        with open("log.txt", "w") as log_file: #Log Datei wird als log_file geöffnet
            while True: #Schleife um Prozess endlos laufen zu lassen
                message, _ = mq_conv_log.receive() #Nachricht empfangen
                value = struct.unpack('i', message)[0] #Nachricht in Integer-Format bringen
                log_file.write(f"{value}\n") #Wert in Log-Datei schreiben
                log_file.flush() #Sicherstellen, dass Werte sofort in Datei geschrieben werden
                time.sleep(2)
    except KeyboardInterrupt: #Beim Beenden des Programms werden Message Queues geschlossen
        mq_conv_log.close()

if __name__ == "__main__":
    log()