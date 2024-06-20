import socket

#empfangen der Stat Daten vom Report Server
def reportHandleClient(clientSocket):
    try:
        while True:
            statValues = clientSocket.recv(1024).decode()
            if not statValues:
                break
            mean, total = statValues.split(',')
            print('[REPORT] mean: ' + mean + '\ntotal: '+ total)
    except Exception as e:
        print('[REPORT] error receiving data from [STAT]')
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
        print(f"Accepted connection from {ClientAddress}")
        reportHandleClient(clientSocket)
        
if __name__ == "__main__":
    reportServer()