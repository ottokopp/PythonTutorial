### WICHTIG ###
# Alle Hausaufgaben grundsätzlich nur in eurer eigenen Git-Branch machen.
# 'git checkout -b "dein_name"' um eine neue Branch zu erstellen.
# Wenn ihr die Hausaufgabe korrigiert haben wollt, get auf die GitHub Seite der Repo, wählt eure Branch aus und drückt auf "Pull Request".


"""
Willkommen zu HA 2. Diesmal arbeiten wir mit Files auf unserem Computer.

Wir beginnen mit dem Lesen von textbasierten Dateien.
der Befehl den du hierfür brauchst lautet:

with open("pfad/zu/deiner/datei.txt") as irgendeine_variable:
    inhalt = irgendeine_variable.read()

1. Versuche nun (erstmal ohne zusätzliches googlen) die Datei "schachverein_mitglieder.csv" zu
öffnen und den Inhalt in einer Variable "chessclub_members" zu speichern.
2. mit der "read()" Methode bekommst du den gesamten Inhalt als String den du in eine Variable speichern kannst.
3. Die Aufgabe ist gelöst, wenn "db. get_members()" einen String zurückgibt, der den Inhalt der Datei enthält und du
"python a1.py" ausführen kannst, um diesen String im Terminal darzustellen.
"""

# Die Klassendefinition kannst du erstmal ignorieren. Wichtig ist für dich im Moment nur, was in get_members() steht, der Rest bleibt, wie er is.
class ChessClubDatabase():
    def __init__(self):
        pass

    def get_members():
        chessclub_members = ""

        # TODO: Hier kommt dein Code zum Einlesen der Datei und speichern in 'chessclub_members'


        return chessclub_members


# Ab hier nichts ändern. Ab hier muss fehlerfrei ausführbar sein.
if __name__ == "__main__":
    db = ChessClubDatabase()
    print(db.get_members())
# Bis hier nichts ändern.

"""
[OPTIONAL für Streberchen] Anmerkungen zu with open(...) etc.

1. "open()" öffnet eine Datei auf eurem Computer und gibt ein von Python nutzbares Datei-Objekt zurück.
(probiert gerne mal 'print(type(open(pfad/zur/datei.txt)))' aus, um zu sehen, wie das aussieht.)
    - open() nimmt die folgenden Parameter an:
    a) Der Pfad zu der Datei die geöffnet werden soll.
    Einen Pfad müsst ihr angeben, sonst weiß Python nicht, welche Datei ihr öffnen wollt.
    b) Der Modus in dem die Datei geöffnet werden soll. Standardmäßig ist dies "r" für "read" (lesen).
    Es gibt auch "w" für "write" (schreiben) und einige andere, je nachdem was ihr tun wollt.
    einen Modus müsst ihr NICHT zwingend angeben, wenn ihr nur lesen wollt, denn "r" ist schon der Standardwert.
    c) Optional könnt ihr auch noch die Kodierung der Datei angeben, z.B. "utf-8" für Unicode Dateien.
    Weil wir deutsche Kartoffeln sind, werden wir das ab und zu brauchen, das erkennt ihr daran, dass
    Umlaute wie "ä", "ö", "ü" und so nicht richtig dargestellt werden. "utf-8" beinhaltet Umlaute und zeigt sie
    daher richtig an.

sprich, wenn ihr eine Datei habt und deutschen Text (mit Umlauten z.b.) erwartet, dann sieht das so aus:

with open("pfad/zu/deiner/datei.txt", "r", encoding="utf-8") as datei_variable:
    inhalt = datei_variable.read()

2. "with" kümmert sich um Betriebssystem-spezifische Dinge wie das korrekte Schließen der Datei
nachdem wir sie verarbeitet haben. Es ist gute, gängige Praxis, open() immer mit "with" zu benutzen.
Es ist selten ein Problem, aber wenn es eins ist, dann ein nerviges.

3. "as" weist das Datei-Objekt, das open() zurückgibt, einer Variable zu. Ohne "as" könnten wir
nicht auf die Datei zugreifen. Ihr könnt die Variable nennen wie ihr wollt. "as" ist quasi im Prinzip
ein Synonym für "=" in diesem Kontext.
Das Folgende würde daher auch funktionieren, aber wir haben nicht die Vorteile von "with"
und könnten eventuell Probleme bekommen, wenn wir die Datei nicht korrekt schließen.

meine_daten = open("pfad/zu/deiner/datei.txt")

4. "read()" ist eine spezielle Methode von Datei-Objekten, die den gesamten Inhalt der Datei auf einmal
in einen String lädt. Es gibt viele Möglichkeiten, Dateien auszulesen, je nachdem was man benötigt.
In der Regel ist Zeilenweises Auslesen mit readlines() oder spezielle libraries wie "csv" oder "json"
die praktikablere Lösung, aber während wir lernen, halte ich es für besser, die einzelnen
Schritte nachzuvollziehen.

"""