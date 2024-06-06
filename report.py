import time

def report():


   

    try:

        while True:

            message, _ = mq_stat_report.receive()

            average, total = struct.unpack('ff', message)

            print(f"average: {average}, Total: {total}")

    except KeyboardInterrupt:

        mq_stat_report.close()
