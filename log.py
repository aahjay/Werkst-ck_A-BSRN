import socket

def logClientSocket():
    while True:
        try:
            logClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logClient.connect(('127.0.0.1', 9998))
            print("Connected to Conv server on port 9998")
            break
        except ConnectionRefusedError:
            print("Waiting for conv server...")
            time.sleep(2)

    with open('log.txt', 'a', buffering = 1) as file: #öffnet eine neue log-Datei (Textdokument) bzw. die bereits im Verzeichnis existierende log-Datei
        while True:
            conv_values = logClient.recv(1024).decode() #empfängt Daten vom Server (in diesem Fall der conv Server, der die generierten Messwerte enthält)
            if not conv_values: #if-Konstruktion für den Fall, dass keine Werte empfangen wurden
                break
            file.write(conv_values + '\n') #schreibt die Werte aus conv in die Datei 'log.txt'
            file.flush()
            print('logged ' + str(conv_values))

if __name__ == "__main__":
    logClientSocket()