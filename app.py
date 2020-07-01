print()
from PySide2 import QtWidgets
import os
import json

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")
        self.DATA_FILE = ""
        self.setup_hmi()        
        self.setup_list()
        self.connections()
        
# Creation de l'interface
    def setup_hmi(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.text_moviename = QtWidgets.QLineEdit()
        self.btn_addmovie = QtWidgets.QPushButton("Add Movie")
        self.list_movies = QtWidgets.QListWidget()
        self.list_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_deletemovie = QtWidgets.QPushButton("Delete Movie")

        self.layout.addWidget(self.text_moviename)
        self.layout.addWidget(self.btn_addmovie)
        self.layout.addWidget(self.list_movies)
        self.layout.addWidget(self.btn_deletemovie)

        CUR_DIR = os.path.dirname(os.path.abspath(__file__))
        self.DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

# Mise à jour de la liste
    def setup_list(self):
        self.list_movies.clear()

        with open(self.DATA_FILE, 'r') as f:
            a = json.load(f)
            
            for movie in a:
                self.list_movies.addItem(movie) 

# Connection des boutons aux fonctions correspondantes
    def connections(self):
        self.btn_addmovie.clicked.connect(self.addmovie)
        self.btn_deletemovie.clicked.connect(self.deletemovie)

# Ajouter un film
    def addmovie(self):
        with open (self.DATA_FILE, 'r+') as f:
            a = json.load(f)
            a.append(self.text_moviename.text())
            f.seek(0)
            json.dump(a, f, indent = 4)
            f.truncate()
            self.setup_list()

# Supprimer des films    
    def deletemovie(self):
        selected_movies = self.list_movies.selectedItems()
        with open(self.DATA_FILE,'r+') as f:
            b = json.load(f)
            print(b)
            for movie in selected_movies:
                b.remove(movie.text())
            f.seek(0)
            json.dump(b, f, indent=4)
            f.truncate()
            self.setup_list()


app = QtWidgets.QApplication([])
fenetre = App()
fenetre.show()
app.exec_()
