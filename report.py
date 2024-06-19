import socket

def reportHandleCLient(clientSocket):
    #entschlüsselt Daten von stat und gibt diese aus
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(data)
    finally:
        client_socket.close()
        

def reportServer():
    #Server um Verbindung zu Stat aufzunehmen
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('0.0.0.0', 10000))
    serverSocket.listen(5)
    while True:
        clientSocket, ClientAddress = serverSocket.accept()
        reportHandleCLient(clientSocket)
        