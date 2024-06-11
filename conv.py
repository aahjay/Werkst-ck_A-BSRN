import time
import random
import threading

#Diese Funktion erstellt zufällige Zahlen, die anschließend in der Konsole ausgegeben werden
def convHandleClient(clientSocket):
    try:
        while True:
            conv_values = random.randint(1, 100)
            #print(str(conv_values))
            clientSocket.sendall(str(conv_values).encode())
            print("sent " + str(conv_values))
            time.sleep(5)
    finally: 
        clientSocket.close()
        
