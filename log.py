import threading

def log():
    with open('log.txt', 'a') as file:
        #if not conv_values:
         #   break
        file.write(conv_values + ' \n')