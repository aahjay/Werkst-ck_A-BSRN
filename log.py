import threading

def log():
    # öffnet eine neue log-Datei (Textdokument) bzw. die bereits im Verzeichnis existierende log-Datei
    with open('log.txt', 'a') as file:
        # schreibt die Werte aus conv in die Datei 'log.txt'
        file.write(conv_values + ' \n')
        print(miau)