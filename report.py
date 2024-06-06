import time

def report():

    try:

        while True:

            value, _ = value_report.receive()

            average, total = struct.unpack('ff', message)

            print(f"average: {average}, Total: {total}")

    except KeyboardInterrupt:

        value_report.close()
