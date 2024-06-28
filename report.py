import time
import posix_ipc
import struct

def report():
    mq_stat_report = posix_ipc.MessageQueue("/mq_stat_report") #Auf Message Queue zugreifen

    try:
        while True: #Schleife um Prozess endlos laufen zu lassen
            message, _ = mq_stat_report.receive() #Nachricht empfangen
            mean, total = struct.unpack('2i', message) #Nachricht in Integer-Format bringen
            print(f"Mean: {mean}, Total: {total}") #Ausgabe auf der Shell
            time.sleep(2)
    except KeyboardInterrupt: #Beim Beenden des Programms werden Message Queues geschlossen
        mq_stat_report.close()