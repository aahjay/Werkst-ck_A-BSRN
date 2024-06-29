import socket
import signal

running = True
def signal_handler(signal, frame):
    global running
    running = False
signal.signal(signal.SIGINT, signal_handler)

#Empfangen und Verarbeiten der Stat Daten vom Report Server
def reportHandleClient(clientSocket):
    try:
        while running:
            statValues = clientSocket.recv(1024).decode()
            if not statValues:
                break
            mean, total = statValues.split(',')
            print('[REPORT] \nmean: ' + mean + '\ntotal: '+ total + '\n')
    except Exception as e:
        print('[REPORT] error receiving data from [STAT]')
    finally:
        clientSocket.close()

#Erstellung Server, um Verbindung zu Stat aufzunehmen
def reportServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(('0.0.0.0', 10000))
    serverSocket.listen(5)
    print("Report server is listening on port 10000")
    while running:
        clientSocket, ClientAddress = serverSocket.accept()
        #print(f"Accepted connection from {ClientAddress}")
        reportHandleClient(clientSocket)
        
if __name__ == "__main__":
    reportServer()