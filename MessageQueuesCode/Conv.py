import random
import time
import posix_ipc
import struct

def conv():
    #Message Queues erstellen
    mq_conv_log = posix_ipc.MessageQueue("/mq_conv_log", posix_ipc.O_CREAT, max_messages=10, max_message_size=128)
    mq_conv_stat = posix_ipc.MessageQueue("/mq_conv_stat", posix_ipc.O_CREAT, max_messages=10, max_message_size=128)   

    try:
        while True: #Schleife um Prozess endlos laufen zu lassen
            value = random.randint(1, 100) #Random Integer erstellen
            mq_conv_log.send(struct.pack('i', value)) #Integer wird eingepackt und an Message Queue gesendet
            mq_conv_stat.send(struct.pack('i', value)) #Integer wird eingepackt und an Message Queue gesendet
            time.sleep(2)
    except KeyboardInterrupt: #Beim Beenden des Programms werden Message Queues geschlossen
        mq_conv_log.close()
        mq_conv_stat.close()

if __name__ == "__main__":
    conv()