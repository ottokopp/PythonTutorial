"""
1. Erstelle einen neuen "git branch" nachdem du diese Repository erfolgreich geklont hast 
(müsste in Whatsapp erklärt haben, wie man die Repository klont) 
    # Benutze dafür den Befehl 'git checkout -b dein-name' in deinem Terminal hier.
    # Ein git branch ist eine Abzweigung der originalen Git-Repository. Das benutzt man, um Code-Änderungen zu machen, ohne an der Hauptapplikaiton direkt
    # etwas zu ändern. Ihr sollt mir eure Lösungen als sogenannten "Pull Request" einreichen. (keine Angst, wird alles erklärt.)
2. Sobald dein branch erstellt ist, führe im Terminal 'git status' aus und ließ, was da steht. Da müsste etwas von "in branch dein-name" stehen.
Wenn da steht "in branch master" oder "main", dann ist das falsch.
3. Führe zum Spaß diese Funktion aus, du musst hier nichts mehr machen.
"""

from time import sleep

def fake_system_failure():
    print("INITIALISIERE SYSTEM WIPE...\n")

    for i in range(3, 0, -1):
        print(f"LÖSCHE ALLE DEINE FILES IN {i}...")
        sleep(1)
    
    print("\nSpaß🙂")

fake_system_failure()