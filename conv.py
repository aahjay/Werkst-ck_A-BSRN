import time
import random
import socket
import threading

#erstellt zufällige Zahlen, die an Log und Stat übermittelt werden
def convHandleClient(clientSocket):
    #try-BLock zum Senden der Daten bzw. Verbindung des Client Socket (Log und Stat) zum Conv Server
    try:
        while True:
            conv_values = random.randint(1, 100)
            clientSocket.sendall(str(conv_values).encode()) #sendet den zuvor mit random generierten Wert verschlüsselt an den verbundenen Client
            print("[CONV] sent " + str(conv_values) + "\n")
            time.sleep(5)
    finally: 
        clientSocket.close() #client Socket wird geschlossen; geht keine Verbindungen mehr ein

#Erstellung Server Socket
def convServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Funktion um Wiederverwendung des Ports zu ermöglichen (Freigabe)
    serverSocket.bind(('0.0.0.0', 9998)) #Bindung des Servers an Adresse und Port
    serverSocket.listen(5) #Server wartet auf eingehende Verbindungen
    print("[CONV] server is listening on port 9998 \n")
    while True:
        clientSocket, clientAddress = serverSocket.accept()  #eingehende Verbindungen von Clients annehmen
        #print(f"Accepted connection from {clientAddress} \n")
        #threading um Verbindung mehrerer Clients gleichzeitig zu ermöglichen (Log und Stat)
        clientThread = threading.Thread(target=convHandleClient, args=(clientSocket,))
        clientThread.start()

if __name__ == "__main__":
    convServer()