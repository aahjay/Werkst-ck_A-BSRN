import time

def report():

    mq_stat_report = posix_ipc.MessageQueue(MQ_STAT_REPORT)

   

    try:

        while True:

            message, _ = mq_stat_report.receive()

            mean, total = struct.unpack('ff', message)

            print(f"Mean: {mean}, Total: {total}")

    except KeyboardInterrupt:

        mq_stat_report.close()
