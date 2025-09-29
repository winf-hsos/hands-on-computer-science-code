# Hands-On Computer Science - Codebeispiele

Dieses GitHub-Repository enthält die Codebeispiele zum Buch [Hands-On Computer Science](https://book.hands-on-computer-science.de) von [Prof. Dr. Nicolas Meseth](https://www.hs-osnabrueck.de/prof-dr-nicolas-meseth/) an der Hochschule Osnabrück.

## Kurzanleitung

1. **Repository klonen**: Klont dieses Repository auf euren lokalen Rechner.
   
   ```bash
   git clone https://github.com/winf-hsos/hands-on-computer-science-code.git
   ```

2. **Python-Umgebung einrichten**: Erstellt eine virtuelle Python-Umgebung und installiert die Abhängigkeiten.
   
   ```bash
   cd hands-on-computer-science-code
   python -m venv .python_env
   .python_env\Scripts\activate # Für Mac/Linux: source .python_env/bin/
   pip install -r requirements.txt
   ```

3. **Eigene Programme schreiben**: Nutzt die Codebeispiele als Grundlage für eure eigenen Programme. Legt eure eigenen Programme in den Ordner `workspace` ab.

4. **Code ausführen**: Führt eure Programme (oder den Beispielcode) in der virtuellen Python-Umgebung aus.
   
   ```bash
   python workspace/euer_programm.py
   ```

5. **Code aktualisieren**: Holt regelmäßig die neuesten Änderungen aus dem Repository.
   
   ```bash
   git pull
   ```