from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import numpy as np
import psycopg2

connection = psycopg2.connect("dbname=Ecommerce user=ceri-commerce password=Elodie host=34.77.160.150 port=5432")
cursorDatabase = connection.cursor()
# nbAlbums=0
# for row in cursorDatabase:
#     nbAlbums+=row[0]
# print(nbAlbums)


def getEverything():
    AllItems=[]

    # query=f'SELECT "nomAlbum", "nomArtiste" FROM public."Album" NATURAL JOIN public."Artiste" WHERE "nomArtiste" = \'{"Smash Into Pieces"}\''
    query = f'SELECT "nomAlbum", "nomArtiste", "imageAlbum", "prixAlbum", "quantiteStockAlbum" FROM public."Album" NATURAL JOIN public."Artiste" ORDER BY "nomArtiste", "nomAlbum" ASC'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        AllItems.append(row[0])
        AllItems.append(row[1])
        AllItems.append(row[2])
        AllItems.append(row[3])
        AllItems.append(row[4])
    print(AllItems)


    Everything=np.zeros((int(len(AllItems)/5),5), dtype=object)
    for i in range(0,int(len(AllItems)/5)):
        for j in range(0,int(len(AllItems)/5)+2):
            Everything[i,j]=AllItems[(i*5)+j]

    print(Everything)
    return Everything.tolist()


def getAlbumByArtist(nomArtiste):
    Albums=[]
    query=f'SELECT "nomAlbum", "imageAlbum", "prixAlbum", "quantiteStockAlbum" FROM public."Artiste" NATURAL JOIN public."Album" WHERE "nomArtiste" =\'{nomArtiste}\'   GROUP BY "nomAlbum","imageAlbum","prixAlbum","quantiteStockAlbum" ORDER BY "nomAlbum" ASC'
    cursorDatabase.execute(query)

    for row in cursorDatabase:
        Albums.append(row[0])
        Albums.append(row[1])
        Albums.append(row[2])
        Albums.append(row[3])
    ListeAlbums=np.zeros((int(len(Albums)/4),4), dtype=object)
    for i in range(0,int(len(Albums)/4)):
        for j in range(0,int(len(Albums)/4)+2):
            ListeAlbums[i,j]=Albums[(i*4)+j]

    return ListeAlbums.tolist()

def getMusicsByArtist(nomArtiste, nomAlbum):
    Musiques=[]
    query=f'SELECT "nomChanson" FROM public."Chanson" NATURAL JOIN public."Album" NATURAL JOIN public."Artiste" WHERE "nomArtiste" =\'{nomArtiste}\' AND "nomAlbum" =\'{nomAlbum}\''
    cursorDatabase.execute(query)
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