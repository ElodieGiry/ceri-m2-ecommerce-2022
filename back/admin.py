import mariadb
import numpy as np
import identifiantsbdd

connection = mariadb.connect(user=identifiantsbdd.username, password=identifiantsbdd.password, database=identifiantsbdd.database, host=identifiantsbdd.host, port=identifiantsbdd.port)
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