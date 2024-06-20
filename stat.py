import time
import posix_ipc
import struct

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
            time.sleep(5)

    except KeyboardInterrupt:
        mq_conv_stat.close()
        mq_stat_report.close()

    
