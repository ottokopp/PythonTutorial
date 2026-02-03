"""
1. Erstelle eine Klasse "Person" mit den Attributen "name" und "beruf".
2. Erstelle eine Klasse "Beruf" mit den Attributen "name" und "erfahrung".
3. Erstelle eine Klasse "Erfahrung" mit dem Attribut "level".
4. Führe diese Datei aus. Sie sollte fehlerfrei ausführbar sein, ohne im gekennzeichneten Bereich etwas zu verändern.
"""

# TODO: Hier deine Klassendefinition.


### AB HIER NICHTS VERÄNDERN, AB HIER MUSS FEHLERFREI AUSFÜHRBAR SEIN ###
kevin = Person("Kevin", Beruf("Mechaniker", Erfahrung("ein Anfänger")))
sigma_siggi = Person("Sigma Siggi", Beruf("Programmierer", Erfahrung("eine Legende")))

print(kevin.name, "ist", kevin.beruf.name, "und", kevin.beruf.erfahrung.level)
print(sigma_siggi.name, "ist", sigma_siggi.beruf.name, "und", sigma_siggi.beruf.erfahrung.level)
### BIS HER NICHTS VERÄNDERN ###