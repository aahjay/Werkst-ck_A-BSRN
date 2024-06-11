import time
import random
import threading
import socket

#Diese Funktion erstellt zufällige Zahlen, die anschließend in der Konsole ausgegeben werden
def convHandleClient(clientSocket):
    #try-BLock zum Senden der Daten bzw. Verbindung des CLient Socket zum Server
    try:
        while True:
            conv_values = random.randint(1, 100)
            #print(str(conv_values))
            clientSocket.sendall(str(conv_values).encode()) #sendet den zuvor mit random generierten Wert verschlüsselt an den Server Socket
            print("sent " + str(conv_values) + "\n")
            time.sleep(5)
    finally: 
        clientSocket.close() #client Socket wird geschlossen; geht keine Verbindungen mehr ein
        
def convServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Erstellung Sever Socket
    serverSocket.bind(('localhost', 9999)) #Bindung des Servers an Adresse und Port
    serverSocket.listen(5) #Server wartet auf eingehende Verbindungen

    while True:
        clientSocket, clientAdress = serverSocket.accept() #eingehende Verbindungen von Clients annehmen
        clientThread = threading.Thread(target=convHandleClient, args=(clientSocket,)) #Erstellung thread für Funktion convHandleCLient()
        clientThread.start() #thread starten

serverThread = threading.Thread(target=convServer) #Erstellung thread für convServer()
serverThread.start() #thread starten