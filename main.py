from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import numpy as np



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
    cursorDatabase.execute("SELECT COUNT(*) FROM Chanson")
    cursorDatabase.execute(f"SELECT Artiste.Nom, Album.NomAlbum, Album.Image, Chanson.Titre FROM Artiste inner join Album on Nom=Album.Artiste inner join Chanson on Chanson.Album=Album.NomAlbum GROUP BY Chanson.Titre ORDER BY Artiste.Nom, NomAlbum") #ORDER BY Artiste.Nom, NomAlbum,

    for row in cursorDatabase:
        AllItems.append(row[0])
        AllItems.append(row[1])
        AllItems.append(row[2])
        AllItems.append(row[3])
    Everything=np.zeros((int(len(AllItems)/4),4), dtype=object)
    for i in range(0,int(len(AllItems)/4)):
        Everything[i][0]=AllItems[i*4]
        Everything[i][1]=AllItems[i*4+1]
        Everything[i][2]=AllItems[i*4+2]
        Everything[i][3]=AllItems[i*4+3]
    # print(Everything)
    # return AllItems
    return Everything.tolist()


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
    # return Albums
    ListeAlbums=np.zeros((int(len(Albums)/2),2), dtype=object)
    for i in range(0,int(len(Albums)/2)):
        ListeAlbums[i][0]=Albums[i*2]
        ListeAlbums[i][1]=Albums[i*2+1]
    return ListeAlbums.tolist()

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


origins = [
    "http://localhost:4200",
    "localhost:4200"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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