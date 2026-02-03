"""
Also, wenn du nach der letzten Aufgabe immer noch Bock hast was zu machen, dann Hut ab.
Dann hoffe ich, bricht diese Aufgabe hier vollends deinen Willen.

Ich gebe dir gar nichts vor. Die Aufgabe ist herauszufinden, was du überhaupt tun musst. Ja, I know, I know. Ich hab gesagt, die ist, um deinen Willen zu brechen.

1. Du bist Battle-Programmer Shirase, ein Privatermittler der mit Hilfe von Python-Code Kriminalfälle löst.
2. Ein Mörder ist auf freiem Fuß. Alles was du von der Polizei bekommen hast, ist eine Datei aus dem Computer des Mörders.
Es scheint wohl eine Art Tagebuch-Eintrag zu sein, aber die Ermittler werden daraus nicht schlau.
Es war der letzte Tagebuch-Eintrag bevor der Mörder verschwunden ist und es ist alles, was wir haben.
3. Mithilfe dieser Datei "HA2/evidence.txt" und deinen 1337-Python Skills, finde heraus:
    - Wie heißt der Mörder und wo hat er die Tat vollzogen?
    - Wen hat der Mörder getötet?
    - Was war die Tatwaffe und wo ist sie versteckt?
    - Wo ist der Mörder jetzt?
4. Du darfst alles machen, was du willst, außer AI benutzen wie ein Kelp.
5. Gib nicht zu schnell auf. Es ist sehr schwer, aber mit dem Wissen, das du hast, möglich.
6. Viel Erfolg, Shirase.
"""

# Du darfst hier alles verändern, was du willst. Das ist nur ein Startpunkt. Viel Spaß :)

with open("HA2/evidence.txt", "r", encoding="utf-8") as file:
    data = file.read()