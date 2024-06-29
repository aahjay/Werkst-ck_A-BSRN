import socket
import signal
import time

running = True
def signal_handler(signal, frame):
    global running
    running = False
signal.signal(signal.SIGINT, signal_handler)

#Erstellung Client Socket zur Verbindung mit Conv
def logClientSocket():
    while running:
        try:
            logClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logClient.connect(('127.0.0.1', 9998))
            print("[LOG] Connected to [CONV] server on port 9998 \n")
            break
        except ConnectionRefusedError:
            print("Waiting for [CONV] server...")
            time.sleep(2)

    # öffnet eine neue log-Datei (Textdokument) bzw. die bereits im Verzeichnis existierende log-Datei
    with open('log.txt', 'a', buffering = 1) as file:
        while running:
            conv_values = logClient.recv(1024).decode() #empfängt Daten vom Conv Server
            if not conv_values:
                break
            file.write(conv_values + '\n') #schreibt die Werte aus conv in die Datei 'log.txt'
            file.flush()
            print('[LOG] logged ' + str(conv_values) + '\n')

if __name__ == "__main__":
    logClientSocket()