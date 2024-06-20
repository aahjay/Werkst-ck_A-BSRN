import random
import time
import posix_ipc
import struct

def conv():
    mq_conv_log = posix_ipc.MessageQueue("/mq_conv_log", posix_ipc.O_CREAT, max_messages=10, max_message_size=128)
    mq_conv_stat = posix_ipc.MessageQueue("/mq_conv_stat", posix_ipc.O_CREAT, max_messages=10, max_message_size=128)   

    try:
        while True:
            value = random.randint(1, 100)
            mq_conv_log.send(struct.pack('i', value))
            mq_conv_stat.send(struct.pack('i', value))
            time.sleep(5)
    except KeyboardInterrupt:
        mq_conv_log.close()
        mq_conv_stat.close()
