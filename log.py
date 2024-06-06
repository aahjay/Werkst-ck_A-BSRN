import threading

with open('log.txt', 'a') as file:
    while True:
        convValues = logClient.recv(1024).decode()
        if not convValues:
            break
        file.write(convValues + ' \n')

