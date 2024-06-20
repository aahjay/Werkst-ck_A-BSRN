import time
import random
import socket
import threading

#Diese Funktion erstellt zufällige Zahlen, die anschließend in der Konsole ausgegeben werden
def convHandleClient(clientSocket):
    #try-BLock zum Senden der Daten bzw. Verbindung des CLient Socket zum Server
    try:
        while True:
            conv_values = random.randint(1, 100)
            print(str(conv_values))
            clientSocket.sendall(str(conv_values).encode()) #sendet den zuvor mit random generierten Wert verschlüsselt an den Server Socket
            print("sent " + str(conv_values) + "\n")
            time.sleep(5)
    finally: 
        clientSocket.close() #client Socket wird geschlossen; geht keine Verbindungen mehr ein
        
def convServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Erstellung Server Socket
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(('0.0.0.0', 9998)) #Bindung des Servers an Adresse und Port
    serverSocket.listen(5) #Server wartet auf eingehende Verbindungen
    print("Conv server is listening on port 9998")
    while True:
        clientSocket, clientAddress = serverSocket.accept()  # eingehende Verbindungen von Clients annehmen
        print(f"Accepted connection from {clientAddress}")
        convHandleClient(clientSocket)

if __name__ == "__main__":
    convServer()