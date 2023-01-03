from fastapi import FastAPI, HTTPException, Form, Query,APIRouter
from fastapi.middleware.cors import CORSMiddleware
import mariadb
import identifiantsbdd
import connexion
import commande
from enum import Enum
from pydantic import BaseModel
import subprocess
from typing import Union
import admin


connection = mariadb.connect(user=identifiantsbdd.username, password=identifiantsbdd.password, database=identifiantsbdd.database, host=identifiantsbdd.host, port=identifiantsbdd.port)
cursorDatabase = connection.cursor()


query=f'SELECT * FROM `album`'
cursorDatabase.execute(query)
nbAlbums=0
for row in cursorDatabase:
    nbAlbums+=row[0]
# print(nbAlbums)

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

    Everything= [0]*int(len(AllItems)/5)
    for i in range(0,int(len(AllItems)/5)):
        Everything[i]=[0]*5
        for j in range(0,int(len(AllItems)/(nbAlbums+2))+4):
            Everything[i][j]=AllItems[(i*5)+j]
    return Everything

def getArtists():
    cursorDatabase = connection.cursor()
    AllArtists=[]
    query=f'SELECT nomArtiste FROM artiste ORDER BY nomArtiste ASC'
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()
    for row in result:
        AllArtists.append(row[0])
        
    cursorDatabase.close()
    # print(AllArtists[0])
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
    cursorDatabase.close()

    ListeAlbums= [0]*int(len(Albums)/4)
    for i in range(0,int(len(Albums)/4)):
        ListeAlbums[i]=[0]*4
        for j in range(0,int(len(Albums)/4)+2):
            ListeAlbums[i][j]=Albums[(i*4)+j]
    return ListeAlbums

def getMusicsByArtist(nomArtiste, nomAlbum):
    cursorDatabase = connection.cursor()
    Musiques=[]
    query=f'SELECT nomChanson FROM chanson NATURAL JOIN album NATURAL JOIN artiste WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\') AND LOWER(nomAlbum) = LOWER(\'{nomAlbum}\') ORDER BY nomChanson'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        Musiques.append(row[0])
    # print(Musiques)
    cursorDatabase.close()
    return Musiques

def getAlbumImage(nomArtiste, nomAlbum):
    imageAlbum=""
    cursorDatabase = connection.cursor()
    query=f'SELECT imageAlbum FROM album NATURAL JOIN artiste WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\') AND LOWER(nomAlbum) = LOWER(\'{nomAlbum}\')'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        imageAlbum=row[0]
    cursorDatabase.close()
    return imageAlbum

def getAlbumPrice(nomArtiste, nomAlbum):
    prixAlbum=""
    cursorDatabase = connection.cursor()
    query=f'SELECT prixAlbum FROM album NATURAL JOIN artiste WHERE LOWER(nomArtiste) = LOWER(\'{nomArtiste}\') AND LOWER(nomAlbum) = LOWER(\'{nomAlbum}\')'
    cursorDatabase.execute(query)
    for row in cursorDatabase:
        prixAlbum=row[0]
    cursorDatabase.close()
    return prixAlbum


def panier(gestionPanier, nomArtiste, nomAlbum, quantite):
    if gestionPanier and nomArtiste and nomAlbum and quantite:
        if gestionPanier=="ajouter":
            return {"L'album "+ nomAlbum+" de " + nomArtiste +" a été ajouté "+ str(quantite) +" fois au panier"}
        elif gestionPanier=="supprimer":
            return {"L'album "+ nomAlbum+" a été supprimé du panier"}


class ItemConnexion(BaseModel):
    email: str
    password: str


class ItemInscription(BaseModel):
    nom: str
    prenom: str
    email: str
    password: str
    telephone: str
    adresse: str
    codePostal: str
    ville: str
    pays: str
    


app = FastAPI()

router = APIRouter()
app.include_router(router)
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
def read_root(gestion: str = None,nomArtiste: str = None, nomAlbum: str = None, quantite: int = None):
    return {"Item": getEverything(), "Panier": panier(gestion, nomArtiste, nomAlbum, quantite)}

# route en post pour se connecter
@app.post("/connexion")
def login(item: ItemConnexion):
    print("---------------------------------------------------------------")
    return {connexion.connexion(item.email, item.password)}

@app.post("/inscription")
def inscription(item: ItemInscription):
    print("---------------------------------------------------------------")
    return {connexion.inscription(item.nom, item.prenom, item.email, item.password, item.telephone, item.adresse, item.codePostal, item.ville, item.pays)}

@app.get("/artistes")
def read_item():
    return {"Artistes": getArtists()}
    
@app.get("/commande")
def read_item(email : str):
    print("---------------------------------------------------------------")
    return {"Email": email, 'Commande': commande.verificationCommande(email)}

@app.get("/admin")
def read_item(idCommande: int = None, etat: str = None):
    print("---------------------------------------------------------------")
    if idCommande == None or etat == None:
        return {"Commandes": admin.recupererCommandes()}
    return {"Commande modifiée ": admin.modifierCommande(idCommande, etat),"Commandes": admin.recupererCommandes()}

# @app.get("/panier")
# def read_item(panier : Union[str, None] = Query(default=None, min_length=3, max_length=50)):
#     print("---------------------------------------------------------------")
#     if panier == "ajouter":
#         return {"Message": "Ajouté au panier"}
#     return {"Message": "Article supprimé du panier"}


@app.get("/{nom_artiste}")
def read_item(nom_artiste: str):
    print("---------------------------------------------------------------")
    return {"Artiste": nom_artiste, 'Albums': getAlbumByArtist(nom_artiste)}


@app.get("/{nom_artiste}/{nom_album}")
def read_item(nom_artiste: str, nom_album: str):
    print("---------------------------------------------------------------")
    return {"Artiste": nom_artiste, 'Musiques': getMusicsByArtist(nom_artiste,nom_album), 'Image': getAlbumImage(nom_artiste,nom_album), 'Prix': getAlbumPrice(nom_artiste,nom_album)}  
