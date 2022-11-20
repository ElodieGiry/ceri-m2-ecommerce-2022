import mariadb
import numpy as np
import identifiantsbdd

connection = mariadb.connect(user=identifiantsbdd.username, password=identifiantsbdd.password, database=identifiantsbdd.database, host=identifiantsbdd.host, port=identifiantsbdd.port)
cursorDatabase = connection.cursor()

def creationCommande(date,montant,etat,emailClient,telephoneClient,adresse,cp,ville,pays):

    query=f'SELECT idClient FROM `client` WHERE emailClient = \'{emailClient}\'' #On récupère l'id du client
    cursorDatabase.execute(query) #On execute la requête
    for row in cursorDatabase:
        idClient=row[0]

    query=f'INSERT INTO `commande`(`dateCommande`, `montantCommande`, `etatCommande`, `idClient`, `telephoneClient`, `adresseLivraison`,  `cpLivraison`, `villeLivraison`, `paysLivraison`) VALUES (\'{date}\',{montant},\'{etat}\',\'{idClient}\',\'{telephoneClient}\',\'{adresse}\',\'{cp}\',\'{ville}\',\'{pays}\')' #On crée la commande
    cursorDatabase.execute(query) #On execute la requête
    connection.commit() #On commit la requête


def creationDetailCommande(idCommande,idAlbum,quantite):
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

# creationCommande('2021-01-01', 20, 'En préparation', 'jcvinyl@gmail.com', '0123456789', '18 rue des cd', '84140', 'Montfavet', 'France')
# creationCommande('2021-01-02', 10, 'En préparation', 'jcvinyl@gmail.com', '0123456789', '18 rue des cd', '84140', 'hrfuhfhu', 'France')
# creationDetailCommande(2,1,1)
# creationDetailCommande(1, 4, 1)
# creationDetailCommande(1, 5, 1)
# print(verificationCommande('jcvinyl@gmail.com'))