import socket

def reportHandleClient():
    while True:
        try:
            repClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            repClient.connect(('127.0.0.1', 9999))
            print("report connected to stat server on port 9999")
            break
        except ConnectionRefusedError:
            print("Waiting for stat server...")
            time.sleep(2)
        while True:
            data = clientSocket.recv(1024).decode()
            if not data:
                break
            mean, total = data.split(',')
            print(data)
        #finally:
         #   clientSocket.close()
        

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
        reportHandleClient(clientSocket)
        
if __name__ == "__main__":
    reportServer()