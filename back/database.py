import mariadb
from os import environ

USER=environ.get("USER")
PASSWORD=environ.get("PASSWORD")
DBNAME=environ.get("DBNAME")
HOST=environ.get("HOST")
MYSQL_PORT=3306

connection = mariadb.connect(user=USER, password=PASSWORD, database=DBNAME, host=HOST, port=int(MYSQL_PORT))