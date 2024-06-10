def stat():
    values = []   # Initialisierung einer leere Liste, um die empfangenen Werte zu speichern
    while True:
        value = ()
         if value:
                value = int(value) # Konvertiert den Wert in einen Ganzzahlwert
                values.append(value) # Fügt den Wert zur Liste der empfangenen Werte hinzu
                mean = sum(values) / len(values)  # Berechnet den Mittelwert der Werte
                total = sum(values) # Berechnet die Summe der Werte

    
