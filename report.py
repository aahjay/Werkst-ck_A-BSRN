import time
import posix_ipc
import struct

def report():
    mq_stat_report = posix_ipc.MessageQueue("/mq_stat_report")

    try:
        while True:
            message, _ = mq_stat_report.receive()
            mean, total = struct.unpack('2i', message)
            print(f"Mean: {mean}, Total: {total}")
            time.sleep(2)
    except KeyboardInterrupt:
        mq_stat_report.close()