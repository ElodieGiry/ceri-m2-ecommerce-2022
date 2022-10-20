from typing import Union

from fastapi import FastAPI
import sqlite3



# faire tests avec pytest

connectionDatabase = sqlite3.connect('vinyles.db', check_same_thread=False)
cursorDatabase = connectionDatabase.cursor()
cursorDatabase.execute("SELECT COUNT(*) FROM Artiste")
nbAlbums=0
for row in cursorDatabase:
    nbAlbums+=row[0]

def getEverything():
    AllItems=[]
    connectionDatabase = sqlite3.connect('vinyles.db', check_same_thread=False)
    cursorDatabase = connectionDatabase.cursor()
    cursorDatabase.execute(f"SELECT Artiste.Nom, Album.NomAlbum, Album.Image, Chanson.Titre FROM Artiste inner join Album on Nom=Album.Artiste inner join Chanson on Chanson.Album=Album.NomAlbum ORDER BY Artiste.Nom, NomAlbum ")
    
    for row in cursorDatabase:
        AllItems.append(row[0])
        AllItems.append(row[1])
        AllItems.append(row[2])
        AllItems.append(row[3])
    print(AllItems)
    return AllItems


def getAlbumByArtist(nomArtiste):
    Albums=[]
    connectionDatabase = sqlite3.connect('vinyles.db', check_same_thread=False)
    cursorDatabase = connectionDatabase.cursor()
    # print(f"SELECT Album, Image FROM Artiste inner join Album on Nom=Artiste WHERE Nom ='{nomArtiste}'")
    cursorDatabase.execute(f"SELECT NomAlbum, Image FROM Artiste inner join Album on Nom=Artiste WHERE Nom ='{nomArtiste}' GROUP BY NomAlbum")
    
    for row in cursorDatabase:
        Albums.append(row[0])
        Albums.append(row[1])
    # print(Albums)
    return Albums

def getMusicsByArtist(nomArtiste, nomAlbum):
    Musiques=[]
    connectionDatabase = sqlite3.connect('vinyles.db', check_same_thread=False)
    cursorDatabase = connectionDatabase.cursor()
    # print(f"SELECT Titre FROM Chanson inner join Artiste on Chanson.Artiste=Artiste.nom WHERE Nom ='{nomArtiste}' AND Artiste.Album = '{nomAlbum}' AND Chanson.Album = '{nomAlbum}'")
    cursorDatabase.execute(f"SELECT Titre FROM Chanson inner join Album on Chanson.Album=NomAlbum inner join Artiste on Album.Artiste=Artiste.nom WHERE Nom ='{nomArtiste}' AND Artiste.Album = '{nomAlbum}' AND Chanson.Album = '{nomAlbum}'")
    
    for row in cursorDatabase:
        Musiques.append(row[0])
    print(Musiques)
    return Musiques


app = FastAPI()

@app.get("/")
def read_root():
    return {"Item": getEverything()}


@app.get("/{nom_artiste}")
def read_item(nom_artiste: str):
    print("---------------------------------------------------------------")
    print(type(nom_artiste))
    return {"Artiste": nom_artiste, 'Albums': getAlbumByArtist(nom_artiste)}


@app.get("/{nom_artiste}/{nom_album}")
def read_item(nom_artiste: str, nom_album: str):
    print("---------------------------------------------------------------")
    print(nom_artiste)
    return {"Artiste": nom_artiste, 'Musiques': getMusicsByArtist(nom_artiste,nom_album)}