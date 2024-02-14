import sqlite3 as sql # we give sqlite3 the name sql 

dbCon = sql.connect("filmdbpt1/filmflix.db") # to connect to sqlite database

dbCursor = dbCon.cursor() #create a cursor object, call its execute method to run sql queries/statements