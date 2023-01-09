import mariadb
import numpy as np
import identifiantsbdd

USER=identifiantsbdd.username
PASSWORD=identifiantsbdd.password
DBNAME=identifiantsbdd.database
HOST=identifiantsbdd.host
MYSQL_PORT=identifiantsbdd.port

connection = mariadb.connect(user=USER, password=PASSWORD, database=DBNAME, host=HOST, port=MYSQL_PORT)
cursorDatabase = connection.cursor()

def recupererCommandes():
    query=f'SELECT idCommande, dateCommande, etatCommande, emailClient, montantCommande, GROUP_CONCAT(nomAlbum) FROM `commande` NATURAL JOIN `detailscommande` NATURAL JOIN `album` NATURAL JOIN `client` GROUP BY idCommande ORDER BY idCommande DESC'
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()
    if len(result) >= 1:
        Commande=[]
        for row in result:
            Commande.append(row[0])
            Commande.append(row[1])
            Commande.append(row[2])
            Commande.append(row[3])
            Commande.append(row[4])
            Commande.append(row[5])
        Commandes=np.zeros((int(len(Commande)/6),6), dtype=object)
        for i in range(0,int(len(Commande)/6)):
            for j in range(0,6):
                Commandes[i,j]=Commande[i*6+j]
        return Commandes.tolist()
    else:
        return ('Aucune commande n\'a été effectuée pour le moment')


def modifierCommande(idCommande, etatCommande):
    query=f'UPDATE `commande` SET etatCommande="{etatCommande}" WHERE idCommande={idCommande}'
    cursorDatabase.execute(query)
    connection.commit()
    return ('La commande a bien été modifiée')

def ajouterAlbum(nomArtiste, prixAlbum, quantiteStockAlbum, anneeAlbum, typeAlbum, nomAlbum, imageAlbum):
    query=f'SELECT idArtiste FROM `artiste` WHERE nomArtiste="{nomArtiste}"'
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()

    query=f'INSERT INTO `album` (idArtiste, prixAlbum, quantiteStockAlbum, anneeAlbum, typeAlbum, nomAlbum, imageAlbum) VALUES ("{result}","{prixAlbum}","{quantiteStockAlbum}","{anneeAlbum}","{typeAlbum}","{nomAlbum}","{imageAlbum}")'
    cursorDatabase.execute(query)
    connection.commit()
    return ('L\'album a bien été ajouté')

def ajouterArtiste(nomArtiste):
    query=f'INSERT INTO `artiste` (nomArtiste) VALUES ("{nomArtiste}")'
    cursorDatabase.execute(query)
    connection.commit()
    return ('L\'artiste a bien été ajouté')

def ajouterChanson(idAlbum, nomChanson):
    query=f'INSERT INTO `chanson` (idAlbum, nomChanson) VALUES ("{idAlbum}","{nomChanson}")'
    cursorDatabase.execute(query)
    connection.commit()
    return ('La chanson a bien été ajoutée')
