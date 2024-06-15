import socket
import time

def stat():
    values = []   # Initialisierung einer leere Liste, um die empfangenen Werte zu speichern
    while True:
        conv_values = client_socket.recv(1024).decode()
        value = ()
        if not conv_values:
            break
        conv_value = int(conv_values) # Konvertiert den Wert in einen Ganzzahlwert
        values.append(conv_value) # Fügt den Wert zur Liste der empfangenen Werte hinzu
        mean = sum(values) / len(values)  # Berechnet den Mittelwert der Werte
        total = sum(values) # Berechnet die Summe der Werte

def statClient(mean, total):
    #Erstellung eiens Clients, der die von Stat verarbeiteten Daten an Report sendet
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))
    client_socket.sendall(str(mean).encode() + str(total).encode())
    client_socket.close()