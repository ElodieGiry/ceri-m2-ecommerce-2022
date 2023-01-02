import mariadb
import hashlib

import identifiantsbdd

import os

p=os.system('start cloud-sql-proxy.exe --credentials-file "Cle GCP.json" ceri-m1-ecommerce-2022:europe-west1:mysql-primary')
print(p)

connection = mariadb.connect(user=identifiantsbdd.username, password=identifiantsbdd.password, database=identifiantsbdd.database, host=identifiantsbdd.host, port=identifiantsbdd.port)
cursorDatabase = connection.cursor()


def inscription(nom, prenom, email, password, telephone, adresse, codePostal, ville, pays):
    encoded=password.encode()
    result = hashlib.sha256(encoded)
    password=result.hexdigest()
    query=f'INSERT INTO `client`(`nomClient`, `prenomClient`, `emailClient`, `mdpClient`, `telephoneClient`, `adresseClient`, `cpClient`, `villeClient`, `paysClient`) VALUES (\'{nom}\',\'{prenom}\',\'{email}\',\'{password}\', \'{telephone}\',\'{adresse}\',\'{codePostal}\',\'{ville}\',\'{pays}\')'
    cursorDatabase.execute(query)
    connection.commit()

def connexion(email, password):
    encoded=password.encode()
    result = hashlib.sha256(encoded)
    password=result.hexdigest()
    query=f'SELECT * FROM `client` WHERE emailClient = \'{email}\' AND mdpClient = \'{password}\''
    cursorDatabase.execute(query)
    result=cursorDatabase.fetchall()
    if len(result) == 1:
        query=f'SELECT prenomClient, nomClient FROM `client` WHERE emailClient = \'{email}\' AND mdpClient = \'{password}\''
        cursorDatabase.execute(query)
        result=cursorDatabase.fetchall()
        return('Bonjour ' + result[0][0]+ ' ' + result[0][1])
    else:
        return('Erreur de connexion, le mail ou le mot de passe est incorrect')
