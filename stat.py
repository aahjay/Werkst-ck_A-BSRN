import socket
import time

#Client Socket, der die Daten vom Conv Server empfängt
def statClientSocket():
    values = []   # Initialisierung einer leeren Liste, um die empfangenen Werte zu speichern
    statClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    statClient.connect(('127.0.0.1', 9998))
    print("[STAT] Connected to [CONV] server on port 9998 \n")

    while True:
        try:
            conv_values = statClient.recv(1024).decode()
            if not conv_values:
                print('[STAT] received no data from [CONV] \n')
                break
            print('[STAT] received ' + conv_values + ' from [CONV] \n')
            conv_value = int(conv_values)  # Konvertiert den Wert in einen Ganzzahlwert
            values.append(conv_value)  # Fügt den Wert zur Liste der empfangenen Werte hinzu
            mean = sum(values) / len(values)  # Berechnet den Mittelwert der Werte
            total = sum(values)  # Berechnet die Summe der Werte
            print(f"[STAT] calculated - Mean: {mean}, Total: {total} \n")
            sendReport(mean, total)
        except Exception as e:
            print('Error receiving data from [CONV] \n')
            break


#Client Socket, der die Daten an Report übermittelt
def sendReport(mean, total):
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(('127.0.0.1', 10000))
        data = f"{mean},{total}"
        clientSocket.sendall(data.encode())
        print('[STAT] sent data to [REPORT] \n')
        clientSocket.close()
    except Exception as e:
        print('Error sending data to [REPORT] \n')

if __name__ == "__main__":
    statClientSocket()

''' while True:  
        try:

            break
        except ConnectionRefusedError:
            print("Waiting for [CONV] server...")
            time.sleep(2) '''

'''def statClient(mean, total):
    #Erstellung eiens Clients, der die von Stat verarbeiteten Daten an Report sendet
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('127.0.0.1', 10000))
    clientSocket.sendall(str(mean).encode() + str(total).encode())
    clientSocket.close()

def statServer():
    #Server, der eingehende Verbindungen von Conv annimmt
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    print("Stat server is listening on port 9999")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        statHandleClient(client_socket)'''


