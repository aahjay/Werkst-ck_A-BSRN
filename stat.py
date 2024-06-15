import socket
import time

def statHandleClient(client_socket):
    values = []   # Initialisierung einer leeren Liste, um die empfangenen Werte zu speichern
    try:
        while True:
            conv_values = client_socket.recv(1024).decode()
            #value = ()
            if not conv_values:
                break
            conv_value = int(conv_values) # Konvertiert den Wert in einen Ganzzahlwert
            values.append(conv_value) # Fügt den Wert zur Liste der empfangenen Werte hinzu
            mean = sum(values) / len(values)  # Berechnet den Mittelwert der Werte
            total = sum(values) # Berechnet die Summe der Werte
            statClient(mean, total)
    finally: client_socket.close()

def statClient(mean, total):
    #Erstellung eiens Clients, der die von Stat verarbeiteten Daten an Report sendet
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('127.0.0.1', 10000))
    clientSocket.sendall(str(mean).encode() + str(total).encode())
    clientSocket.close()

def statServer():
    #Server, der eingehende Verbindungen von Report anzunehmen
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    while True:
        client_socket, client_address = server_socket.accept()