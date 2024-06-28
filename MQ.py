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
            time.sleep(1)
    except KeyboardInterrupt:
        mq_conv_log.close()
        mq_conv_stat.close()

def log():
    mq_conv_log = posix_ipc.MessageQueue("/mq_conv_log")

    try:
        with open("log.txt", "w") as log_file:
            while True:
                message, _ = mq_conv_log.receive()
                value = struct.unpack('i', message)[0]
                log_file.write(f"{value}\n")
                log_file.flush()
                time.sleep(1)
    except KeyboardInterrupt:
        mq_conv_log.close()

def stat():

    mq_conv_stat = posix_ipc.MessageQueue("/mq_conv_stat")
    mq_stat_report = posix_ipc.MessageQueue("/mq_stat_report", posix_ipc.O_CREAT, max_messages=10, max_message_size=128)

    try:
        values = []
        while True:
            message, _ = mq_conv_stat.receive()
            value = struct.unpack('i', message)[0]
            values.append(value)
           
            mean = sum(values) / len(values)
            total = sum(values)
            mq_stat_report.send(struct.pack('2i', int(mean), total))
            time.sleep(1)

    except KeyboardInterrupt:
        mq_conv_stat.close()
        mq_stat_report.close()


def report():
    mq_stat_report = posix_ipc.MessageQueue("/mq_stat_report")

    try:
        while True:
            message, _ = mq_stat_report.receive()
            mean, total = struct.unpack('2i', message)
            print(f"Mean: {mean}, Total: {total}")
            time.sleep(1)
    except KeyboardInterrupt:
        mq_stat_report.close()