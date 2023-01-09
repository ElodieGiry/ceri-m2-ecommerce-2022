import mariadb
import numpy as np
import os
from os.path import  join, dirname
from dotenv import load_dotenv

import identifiantsbdd
connection = mariadb.connect(user=identifiantsbdd.username, password=identifiantsbdd.password, database=identifiantsbdd.database, host=identifiantsbdd.host, port=identifiantsbdd.port)
cursorDatabase = connection.cursor()

def creationCommande(date,montant,emailClient,telephoneClient,adresse,cp,ville,pays):

    query=f'SELECT idClient FROM `client` WHERE emailClient = \'{emailClient}\'' #On récupère l'id du client
    cursorDatabase.execute(query) #On execute la requête
    for row in cursorDatabase:
        idClient=row[0]

    query=f'INSERT INTO `commande`(`dateCommande`, `montantCommande`, `etatCommande`, `idClient`, `telephoneClient`, `adresseLivraison`,  `cpLivraison`, `villeLivraison`, `paysLivraison`) VALUES (\'{date}\',{montant},En préparation,\'{idClient}\',\'{telephoneClient}\',\'{adresse}\',\'{cp}\',\'{ville}\',\'{pays}\')' #On crée la commande
    cursorDatabase.execute(query) #On execute la requête
    connection.commit() #On commit la requête


def creationDetailCommande(idAlbum,quantite):
    query1=f'SELECT MAX(idCommande) FROM `commande`' #On récupère l'id de la commande
    cursorDatabase.execute(query1) #On execute la requête
    for row in cursorDatabase:
        idCommande=row[0]
    print(idCommande)

    query=f'INSERT INTO `detailscommande`(`idCommande`, `idAlbum`, `quantite`) VALUES ({idCommande},{idAlbum},{quantite})'
    cursorDatabase.execute(query)
    connection.commit()

def verificationCommande(emailClient):
    Commande=[]
    # query=f' SELECT idCommande, nomAlbum FROM `commande` NATURAL JOIN `detailscommande` NATURAL JOIN `album` WHERE idClient = (SELECT idClient FROM `client` WHERE emailClient = \'{emailClient}\') GROUP BY idCommande ORDER BY idCommande DESC'
    query=f'SELECT idCommande, dateCommande, etatCommande, montantCommande, GROUP_CONCAT(nomAlbum) FROM `commande` NATURAL JOIN `detailscommande` NATURAL JOIN `album` WHERE idClient = (SELECT idClient FROM `client` WHERE emailClient = \'{emailClient}\') GROUP BY idCommande ORDER BY idCommande DESC'
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()
    if len(result) >= 1:
        for row in result:
            Commande.append(row[0])
            Commande.append(row[1])
            Commande.append(row[2])
            Commande.append(row[3])
            Commande.append(row[4])
        # cursorDatabase.close()
        Commandes=np.zeros((int(len(Commande)/5),5), dtype=object)
        for i in range(0,int(len(Commande)/5)):
            for j in range(0,int(len(Commande)/(len(result)+2))+3):
                Commandes[i,j]=Commande[(i*5)+j]
        return Commandes.tolist()

        # return Commande
    else:
        return ('Aucune commande n\'a été effectuée pour le moment')
