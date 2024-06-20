import socket
import time

def statHandleClient():
    values = []   # Initialisierung einer leeren Liste, um die empfangenen Werte zu speichern

    while True:
        try:
            convClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            convClient.connect(('127.0.0.1', 9998))
            print("stat Connected to Conv server on port 9998")
            conv_values = convClient.recv(1024).decode()
            #value = ()
            if not conv_values:
                break
            conv_value = int(conv_values) # Konvertiert den Wert in einen Ganzzahlwert
            values.append(conv_value) # Fügt den Wert zur Liste der empfangenen Werte hinzu
            mean = sum(values) / len(values)  # Berechnet den Mittelwert der Werte
            total = sum(values) # Berechnet die Summe der Werte
            print(f"Stat calculated - Mean: {mean}, Total: {total}")
            convClient.sendall(str(mean).encode() + str(total).encode())
            print("Stat sent to Conv server")
            statClient(mean, total)
        finally:
            convClient.close()

def statClient(mean, total):
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
        statHandleClient(client_socket)


if __name__ == "__main__":
    statHandleClient()