# Allgemein

1. Die Hausaufgaben sind grundsätzlich freiwillig (der ganze Kurs ist grundsätzlich freiwillig, aber die Hausi ist nochmal freiwilliger :))
**Du solltest maximal 15-30 Minuten an einer HA verbringen.** Es macht keinen Sinn, seinen Kopf stundenlang gegen die Wand zu schlagen, wenn man nicht weiterkommt.

# Herangehensweise

1. Benutze grundsätzlich immer git und venv für alles, das muss dir in Fleisch und Blut übergehen. (Scroll nach unten für eine Erklärung wie das Git-Setup für die HA funktioniert.)
2. Versuch es zuerst ohne Hilfsmittel, du solltest alle Information die du brauchst schon haben.
3. Wenn du nach ~5 min immer noch auf dem Schlauch stehst, versuch' Google (ohne AI).
4. Wenn immer noch auf dem Schlauch, überspring' die Frage einfach. Ich brauch hier keine AI-Lösung oder sonst irgendwas. Es besser für mich, wenn ich weiß, wo noch Lücken sind, als dass ich weiß, wie schlau ChatGPT ist.
5. Unfertig/halb-fertig aber irgendwie versucht ist 10000% besser als fertig und von irgendwo rauskopiert.


# Git-Setup für HA
![ScreenShot](/_bilder/img1.PNG)
Wenn du die "PythonTutorial"-Repository von git noch nicht auf deinen Rechner geklont hast, dann such dir einen freien, **leeren** Ordner aus (oder mach einen neuen, kannst ihn nennen, wie du willst), wo die rein soll. 
Rechtsklick diesen Ordner, drücke auf "Git bash" (siehe Bild) und in dem erscheinenden Terminal, gib folgenden Befehl ein:
```
git clone git@github.com:ottokopp/PythonTutorial.git
```
![ScreenShot](/_bilder/img2.PNG)
![ScreenShot](/_bilder/img3.PNG)
![ScreenShot](/_bilder/img4.PNG)
Wenn du die Repo schonmal geklont hast und schon auf deinem Rechner hast, kannst du wie oben mit Rechtklick auf den Ordner -> "Git bash" das Terminal für den Ordner öffnen und musst nur die aktuellste Version runterziehen. Das machst du, in dem du auf die Haupt-"Branche" wechselst und "pullst", so wie hier:
```
git checkout master
git pull
```
![ScreenShot](/_bilder/img5.PNG)
![ScreenShot](/_bilder/img6.PNG)
Dann, falls du noch keinen ".venv" Ordner in deinem Projekt hast, erstelle einen mit (das geht in jedem Terminal, das im richtigen Ordner geöffnet ist. Kannst du in Git Bash machen, wo du gerade git pull ausgeführt hast. Oder später im VsCode Terminal.)
```
python -m venv .venv
```
Wenn du schon einen hast, einfach aktivieren mit
```
.venv\Scripts\activate
```
(Scheinbar gibt es bei manchen von euch so ein Windows-Ding, dass dir nicht erlaubt, dieses Script auszuführen. Meldet euch dann einfach bei mir.)