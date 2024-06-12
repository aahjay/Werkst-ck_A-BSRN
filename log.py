import threading
import socket

def logClientSocket():
    logClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logClient.connect(('127.0.0.1', 9999))
    with open('log.txt', 'a') as file: #öffnet eine neue log-Datei (Textdokument) bzw. die bereits im Verzeichnis existierende log-Datei
        while True:
            conv_values = logClient.recv(1024).decode() #empfängt Daten vom Server (in diesem Fall der conv Server, der die generierten Messwerte enthält)
            if not conv_values: #if-Konstruktion für den Fall, dass keine Werte empfangen wurden
                break
            file.write(conv_values + '\n') #schreibt die Werte aus conv in die Datei 'log.txt'
            print('logged ' + str(conv_values))

logThread = threading.Thread(target=logClientSocket) #thread für logCLientSocket()
logThread.start()