import mariadb
from os import environ

USER=environ.get("USER")
PASSWORD=environ.get("PASSWORD")
DBNAME=environ.get("DBNAME")
MYSQL_PORT=3306

connection = mariadb.connect(user=USER, password=PASSWORD, database=DBNAME, unix_socket= "/cloudsql/ceri-m1-ecommerce-2022:europe-west1:mysql-primary", port=int(MYSQL_PORT))
