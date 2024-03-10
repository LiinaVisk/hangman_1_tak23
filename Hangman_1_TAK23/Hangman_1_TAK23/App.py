# App.py
import os.path
import sys
from Controller import Controller

class App:
    def __init__(self, db):
        self.controller = Controller(db)  # Säilita kontrolleri objekt
        self.controller.main()

if __name__ == "__main__":
    db_name = None
    if len(sys.argv) == 2:  # Kontrollib, kas on 2 argumenti, 1. olemas üks sisestamisel
        if os.path.exists(sys.argv[1]):
            db_name = sys.argv[1]
    app = App(db_name)  # Säilita rakenduse objekt
