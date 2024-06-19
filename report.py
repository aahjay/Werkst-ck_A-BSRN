import socket

def reportHandleCLient(clientSocket):
    #entschlüsselt Daten von stat und gibt diese aus
    try:
        while True:
            data = clientSocket.recv(1024).decode()
            if not data:
                break
            mean, total = data.split(',')
            print(data)
    finally:
        clientSocket.close()
        

def reportServer():
    #Server um Verbindung zu Stat aufzunehmen
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(('0.0.0.0', 10000))
    serverSocket.listen(5)
    print("Report server is listening on port 10000")
    while True:
        clientSocket, ClientAddress = serverSocket.accept()
        print(f"Accepted connection from {addr}")
        reportHandleCLient(clientSocket)
        
if __name__ == "__main__":
    reportServer()