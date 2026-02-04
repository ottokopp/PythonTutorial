"""
1. Erstelle einen Virtual Environment in diesem Verzeichnis (google wie man das macht :) )
2. Aktiviere den Virtual Environment im Terminal (.venv/Scripts/activate)
ls -> cd .venv -> ls-> cd Scripts -> .\activate.ps1
deactivate fuer stopen
2. Installiere 'numpy' in diesem Virtual Environment (NICHT in deinem System python). Benutze hierfür den 'pip' Befehl im Terminal (und google den Rest :) )
pip install numpy , installiert in site-packages
4. Ergänze den nötigen import in dieser Datei damit numpy (inklusive der Abkürzung 'np') importiert wird.
5. Führe diese Datei aus und prüfe, ob die Ausgabe korrekt ist.
"""

# TODO: Hier solltest du numpy importieren.
import numpy as np

### AB HIER NICHTS VERÄNDERN ###
print(np.array([1, 2, 3]))
### BIS HER NICHTS VERÄNDERN ###