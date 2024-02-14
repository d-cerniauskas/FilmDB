from connect import *

def read_films():
    # select all films from the films table
    dbCursor.execute("SELECT * FROM tblFilms")

    # fetch all selected records using the fetchall method 
    allRecords = dbCursor.fetchall()

    # lopp through all the fetch records from the films table

    for aFilm in allRecords:
        # displays each record
        print(aFilm)

if __name__ == "__main__":
    read_films()