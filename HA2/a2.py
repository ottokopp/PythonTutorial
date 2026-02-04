"""
In HA2 üben wir zum ersten mal, Code richtig wiederzuverwenden. Ein guter Programmierer codet dieselbe
Funktion niemals zweimal. Und wenn zwei Funktionen ähnlich, aber nicht ganz gleich sein,
überlegt sich ein guter Programmierer wie man eine Funktion so schreiben kann, dass sie in beiden
Fällen funktioniert.

Single Source of Truth (SSOT) Prinzip.

1. In dieser zweiten Aufgabe sollst du die "get_members()" Funktion aus a1.py importieren und benutzen,
ohne ihre Definition hier zu verändern.
2. Wenn du a1.py wie im Beispiel vorgegeben mit read() gelöst hast, dann gibt dir "get_members()" einen String zurück.
Das wollen wir hier nicht. Wir wollen eine Liste mit Eintrag pro Mitglied. Aber anstatt die Funktion jetzt hier
so ähnlich nochmal zu schreiben, wenden wir das SSOT-Prinzip an.
3. Passe "get_members()" in a1.py (nicht hier!!!) so an, dass sie einen Parameter "as_list" annimmt.
4. Lasse "as_list" standardmäßig auf False stehen, sodass sich das Verhalten von "get_members()" für a1.py
nicht ändert! Dein alter Code soll ja auch weiterhin noch funktionieren, wie gewohnt!

Standardwerte gibt man Parametern so:

    def meine_funktion(mein_parameter="mein_standardwert"): # Standardwert muss kein String sein, es kann jede Art von Datentyp sein z.b. boolean im Falle von "as_list"
        print(mein_parameter)

meine_funktion() # Das hier printet dir "mein_standardwert".
meine_funktion("Hallo Welt") # Das hier printet dir "Hallo Welt".
        
5. in get_members() ergänzt du nun den Code so, dass du ein if-Statement einfügst, mit folgenden Möglichkeiten:
    a) Falls "as_list" False ist, führst du get_members() aus, wie du es in a1.py urprünglich geschrieben hattest (mit read() und erhälst einen String.)
    b) Falls "as_list" True ist:
        -> Benutzt du stattdessen die "readlines()" Methode, um den Inhalt der Datei zeilenweise in eine Liste zu laden.
        -> gibst statt dem String von a) diese Liste zurück.

Sprich:

db = ChessClubDatabase()
db.get_members() # du erhälst einen String.
db.get_members(as_list=True) # du erhälst eine Liste.

6. Sowohl a1.py muss noch richtig ausführbar wie vorher, als String, als auch a2.py hier als List.
"""

# IN DIESER DATEI SCHREIBST DU GAR KEINEN CODE. DU HAST ES GESCHAFFT, WENN SIE OHNE ÄNDERUNGEN FEHLERFREI AUSFÜHRBAR IST UND EINE LISTE PRINTET.
if __name__ == "__main__":
    from HA2.a1 import ChessClubDatabase

    db = ChessClubDatabase()
    print(db.get_members(as_list=True))



"""
Noch ein optionaler Streberanmerkungs-Block.

Wie sinnvoll es ist, den return-Wert einer Funktion nach Parameter-Typ zu verändern, ist ein bisschen fortgeschritteneres Python-Fu.
Wenn der Use-Case wie oben beschrieben tatsächlich aufkommt, wäre es wohl auch sinnvoller, statt String oder List ein Python-Objekt zu definieren, dass sowohl den
String als auch den List-case abdeckt.
Für jetzt ist es kein Problem und auch in Production-Code benutze ich solche Konstruktionen ab und zu. Es ist eine der Stärken von Python,
frei seine Typen hin und her zu wechseln, wie man sie gerade braucht, also warum sollte ich das nicht nutzen.
Da haben andere Progrommierer, vor allem, die aus anderen, strenger typisierten Sprachen kommen, eine andere Meinung.
Aber die haben nur Schiss vor dem dynamischen Typ-System von Python, da muss man mehr mitdenken :)
"""
