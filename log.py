import time
import posix_ipc
import struct

def log():
    mq_conv_log = posix_ipc.MessageQueue("/mq_conv_log")

    try:
        with open("log.txt", "w") as log_file:
            while True:
                message, _ = mq_conv_log.receive()
                value = struct.unpack('i', message)[0]
                log_file.write(f"{value}\n")
                log_file.flush()
                time.sleep(2)
    except KeyboardInterrupt:
        mq_conv_log.close()
