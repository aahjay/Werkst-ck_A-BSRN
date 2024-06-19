import socket

def reportHandleCLient(client_socket):
    #entschlüsselt Daten von stat und gibt diese aus
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(data)
    finally:
        client_socket.close()
        
        
