from typing import Union

from fastapi import FastAPI
import sqlite3

connectionDatabase = sqlite3.connect('vinyles.db', check_same_thread=False)
cursorDatabase = connectionDatabase.cursor()
cursorDatabase.execute("SELECT COUNT(*) FROM Artiste")
nbAlbums=0
for row in cursorDatabase:
    nbAlbums+=row[0]

def getAlbumByArtist(nomArtiste):
    Albums=[]
    connectionDatabase = sqlite3.connect('vinyles.db', check_same_thread=False)
    cursorDatabase = connectionDatabase.cursor()
    # print(f"SELECT Album, Image FROM Artiste inner join Album on Nom=Artiste WHERE Nom ='{nomArtiste}'")
    cursorDatabase.execute(f"SELECT Album, Image FROM Artiste inner join Album on Nom=Artiste WHERE Nom ='{nomArtiste}'")
    
    for row in cursorDatabase:
        Albums.append(row[0])
        Albums.append(row[1])
    print(Albums)
    return Albums

def getMusicsByArtist(nomArtiste, nomAlbum):
    Musiques=[]
    connectionDatabase = sqlite3.connect('vinyles.db', check_same_thread=False)
    cursorDatabase = connectionDatabase.cursor()
    print(f"SELECT Titre FROM Chanson inner join Artiste on Chanson.Artiste=Artiste.nom WHERE Nom ='{nomArtiste}' AND Artiste.Album = '{nomAlbum}'")
    cursorDatabase.execute(f"SELECT Titre FROM Chanson inner join Album on Chanson.Album=NomAlbum inner join Artiste on Album.Artiste=Artiste.nom WHERE Nom ='{nomArtiste}' AND Artiste.Album = '{nomAlbum}'")
    
    for row in cursorDatabase:
        Musiques.append(row[0])
    print(Musiques)
    return Musiques


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "Nombre d'albums":nbAlbums}


@app.get("/artiste/{nom_artiste}")
def read_item(nom_artiste: str):
    print("---------------------------------------------------------------")
    print(type(nom_artiste))
    return {"Artiste": nom_artiste, 'Albums': getAlbumByArtist(nom_artiste)}


@app.get("/artiste/{nom_artiste}/{nom_album}")
def read_item(nom_artiste: str, nom_album: str):
    print("---------------------------------------------------------------")
    print(nom_artiste)
    return {"Artiste": nom_artiste, 'Musiques': getMusicsByArtist(nom_artiste,nom_album)}