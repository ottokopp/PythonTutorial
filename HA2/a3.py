"""
!!! WICHTIGE ANMERKUNG ANFANG !!!
WIR SCHREIBEN IMMER NOCH HIER KEINEN CODE REIN! WIR PASSEN ALLES IN a1.py AN!
HIER FÜHREN WIR WIEDER NUR AUS

Diese Aufgabe ist richtig schwer, also lass dir Zeit und mach dir kein Stress.
SCHAU DIR ZUERST DAS BEISPIEL AN, LIEß DORT DIE KOMMENTARE UND LIEß DANN ERST DIESE AUFGABE HIER DURCH, DANN WIRD ES MEHR SINN MACHEN.
!!! WICHTIGE ANMERKUNG ENDE !!!
"""

####################
### DAS BEISPIEL ###
####################
# findest du unter _beispiele/frucht.py

"""
1. Erstelle nun in a1.py eine Klasse namens "ChessClubMember". Schau in die Kopfzeile des .csv file, welche Attribute ein ChessClubMember braucht. (Vorname, Nachname, ELO etc.)

2. Passe in a1.py die "get_members()" Funktion so an, dass sie eine "as_objects" Parameter annimmt, der standardmäßig auf False steht.
Ähnlich wie in a2.py mit "as_list", soll "get_members()" nun folgendes Verhalten haben:
    -> Falls weder "as_list" noch "as_objects" True sind, verhält sich "get_members()" wie in a1.py zuvor und gibt einen String zurück.
    -> Falls "as_objects" True ist, soll "get_members()" eine Liste von ChessClubMember Objekten zurückgeben, die aus den Daten der .csv Datei erstellt wurden.
        (Gehe hierfür erstmal einfach davon aus, dass eine "create_member_from_csv_line(line)" Funktion existiert, die aus einer String-Zeile der .csv Datei 
        ein ChessClubMember Objekt erstellt. Wir werden sie in 3. bauen. Man muss hier gedanklich an zwei Dinge gleichzeitig denken, 
        deswegen die Warnung oben, dass die Aufgabe schwierig ist.)
    -> Falls "as_list" True ist, soll "get_members()" wie es in a2.py vorher war eine Liste von Strings zurückgeben, jeweils ein Eintrag pro Mitglied.
    (-> Falls sowohl "as_list" als auch "as_objects" True sind, soll "as_objects" Vorrang haben und eine Liste von Objekten zurückgegeben werden. Das machst du in dem
    du in der Kette von if-elif-else-statements zuerst auf "as_objects" prüfst.)

Sprich:
get_members() # du erhälst einen String.
get_members(as_list=True) # du erhälst eine Liste von Strings.
get_members(as_objects=True) # du erhälst eine Liste von ChessClubMember Objekten.
get_members(as_list=True, as_objects=True) # du erhälst eine Liste von ChessClubMember Objekten.

3. Erstelle in a1.py eine Funktion namens "create_member_from_csv_line(line)", die eine Zeile aus der .csv Datei annimmt (als String) und daraus ein ChessClubMember Objekt erstellt und zurückgibt.
Du schreibst quasi an der Stelle, an der du mit readlines() einzelne Zeilen als String annimst eine kleine Verarbeitungsschleife die Strings aufsplitten kann
und damit fütterst du dann die Parameter des Konstruktors von ChessClubMember. (Falls du das Beispiel noch nicht angeschaut hast, mach es spätestens jetzt.)

4. Checke ob a1.py, a2.py UND a3.py noch immer genau so funktionieren, wie sie immer funktioniert haben. Die Aufgabe ist erst bestanden, wenn alle 3 Aufgaben
noch fehlerfrei ausführbar sind und die erwarteten Ergebnisse liefern.
"""

### In dieser Datei nichts anfassen, nur ausführen! ###
if __name__ == "__main__":
    from a1 import ChessClubDatabase
    db = ChessClubDatabase()
    print(db.get_members(as_objects=True))
########################################################