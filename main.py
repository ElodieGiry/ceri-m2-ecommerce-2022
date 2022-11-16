from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import numpy as np
import psycopg2
import mysql.connector

DATABASE_USERNAME=""
DATABASE_PASSWORD=""
DATABASE_HOST=""
DATABASE_PORT=""
DATABASE_NAME=""


# connection = psycopg2.connect("dbname=Ecommerce user=ceri-commerce password=Elodie host=34.77.160.150 port=5432")
# connection = psycopg2.connect("dbname=Vinyles user=ceri-commerce password=Elodie host=34.77.160.150 port=5432")
connection = mysql.connector.connect(user='ceri-commerce', password='Elodie', host='localhost', database='Vinyles', port=3306)
cursorDatabase = connection.cursor()




query=f'SELECT * FROM `album`'
cursorDatabase.execute(query)
nbAlbums=0
for row in cursorDatabase:
    nbAlbums+=row[0]
print(nbAlbums)

def getEverything():
    cursorDatabase = connection.cursor()
    AllItems=[]
    query=f'SELECT nomAlbum, nomArtiste, imageAlbum, prixAlbum, quantiteStockAlbum FROM album NATURAL JOIN artiste ORDER BY nomArtiste, nomAlbum ASC'
    
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()
    for row in result:
        AllItems.append(row[0])
        AllItems.append(row[1])
        AllItems.append(row[2])
        AllItems.append(row[3])
        AllItems.append(row[4])
    cursorDatabase.close()

    Everything=np.zeros((int(len(AllItems)/5),5), dtype=object)
    for i in range(0,int(len(AllItems)/5)): 
        for j in range(0,int(len(AllItems)/(nbAlbums+2))+4): 
            Everything[i,j]=AllItems[(i*5)+j]
    return Everything.tolist()
    # return AllItems


def getArtists():
    cursorDatabase = connection.cursor()
    AllArtists=[]
    query=f'SELECT nomArtiste FROM artiste ORDER BY nomArtiste ASC'
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()
    for row in result:
        AllArtists.append(row[0])
        
    cursorDatabase.close()
    print(AllArtists[0])
    return AllArtists



def getAlbumByArtist(nomArtiste):
    cursorDatabase = connection.cursor()
    Albums=[]
    query=f'SELECT nomAlbum, imageAlbum, prixAlbum, quantiteStockAlbum FROM artiste NATURAL JOIN album WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\')   GROUP BY nomAlbum, imageAlbum, prixAlbum, quantiteStockAlbum ORDER BY nomAlbum ASC'
    cursorDatabase.execute(query)

    for row in cursorDatabase:
        Albums.append(row[0])
        Albums.append(row[1])
        Albums.append(row[2])
        Albums.append(row[3])
    ListeAlbums=np.zeros((int(len(Albums)/4),4), dtype=object)
    for i in range(0,int(len(Albums)/4)):
        for j in range(0,int(len(Albums)/4)+3):
            ListeAlbums[i,j]=Albums[(i*4)+j]
    cursorDatabase.close()
    return ListeAlbums.tolist()



def getMusicsByArtist(nomArtiste, nomAlbum):
    cursorDatabase = connection.cursor()
    Musiques=[]
    query=f'SELECT nomChanson, imageAlbum FROM chanson NATURAL JOIN album NATURAL JOIN artiste WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\') AND LOWER(nomAlbum) = LOWER(\'{nomAlbum}\') ORDER BY nomChanson'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        Musiques.append(row[0])
    # print(Musiques)
    cursorDatabase.close()
    return Musiques

def getAlbumImage(nomArtiste, nomAlbum):
    cursorDatabase = connection.cursor()
    query=f'SELECT imageAlbum FROM album NATURAL JOIN artiste WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\') AND LOWER(nomAlbum) = LOWER(\'{nomAlbum}\')'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        imageAlbum=row[0]
    cursorDatabase.close()
    return imageAlbum


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
    return {"Artiste": nom_artiste, 'Albums': getAlbumByArtist(nom_artiste)}


@app.get("/artistes")
def read_item():
    return {"Artistes": getArtists()}


@app.get("/{nom_artiste}/{nom_album}")
def read_item(nom_artiste: str, nom_album: str):
    print("---------------------------------------------------------------")
    return {"Artiste": nom_artiste, 'Musiques': getMusicsByArtist(nom_artiste,nom_album), 'Image': getAlbumImage(nom_artiste,nom_album)}