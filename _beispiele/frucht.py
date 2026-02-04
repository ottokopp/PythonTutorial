class Frucht:
    def __init__(self, name, farbe, gewicht, anzahl):
        self.name = name
        self.farbe = farbe
        self.gewicht = gewicht
        self.anzahl = anzahl

    def __repr__(self):
        # Gibt eine lesbare Darstellung der Frucht zurück, wenn wir ein Frucht Objekt printen.
        # Wenn wir das nicht definieren, bekommen wir sowas wie "<class 'Frucht' object at 0x000001F4C8B1D4C0>"
        # Hiermit bekommen wir stattdessen "Apfel (Rot): 5 Stück, je 200g". Das ist in der Regel nützlicher.
        return f"{self.name} ({self.farbe}): {self.anzahl} Stück, je {self.gewicht}g"

def create_fruit_from_csv_line(line):
    parts = line.split(",")  # splitte den String an jedem Komma
      # 'parts' ist nun eine Liste von Strings. Also wenn line der String "Apfel,Rot,200,5" war, dann ist parts jetzt ["Apfel", "Rot", "200", "5"]
    name = parts[0] # Wir wissen an welchen Stellen, welche Information steht, da wir die Kopfzeile des .csv files kennen.
                      # parts = ["Apfel", "Rot", "200", "5"], also ist parts[0] "Apfel", parts[1] "Rot" usw.
    farbe = parts[1]
    gewicht = int(parts[2]) # cast to int ist optional, aber sinnvoll, wenn wir wissen, dass der Wert eine Zahl ist.
    anzahl = int(parts[3])

    new_fruit = Frucht(name, farbe, gewicht, anzahl) # Wir erstellen ein Frucht-Objekt mit den Informationen, die wir aus der CSV-Zeile extrahiert haben.
    return new_fruit # Wir geben das Frucht-Objekt zurück.

def get_fruits_as_objects():
    fruits = [] # initialisiere eine leere Liste, die wir mit Inhalt füllen wollen.
    with open("obst.csv", "r", encoding="utf-8") as file:
        lines = file.readlines() # readlines() gibt uns eine Liste von Strings, jede Zeile der Datei ist ein Eintrag in der Liste.
        for line in lines[1:]:  # Iteriere über alle Zeilen, überspringe die Kopfzeile
            fruit = create_fruit_from_csv_line(line) # erzeuge ein Frucht-Objekt aus der String-Zeile (siehe oben)
            fruits.append(fruit) # füge das Frucht-Objekt der Liste hinzu
    return fruits