from connect import * 

def delete_films():
    # Fields: title, release date, rating, duration and genre
    # use the primary key to delete the record
    idField = input("Enter the filmID of the record to be deleted: ")

    # DELETE FROM tblFilms WHERE filmID = 1, 2, 3, 4...
    dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    dbCon.commit()

    print(f"Record {idField} deleted from the films table.")

if __name__ == "__main__":
    delete_films()
