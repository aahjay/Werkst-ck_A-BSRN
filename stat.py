import socket
import time

#Client Socket, der die Daten vom Conv Server empfängt
def statClientSocket():
    values = []   # Initialisierung einer leeren Liste, um die empfangenen Werte zu speichern
    statClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(3)
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




