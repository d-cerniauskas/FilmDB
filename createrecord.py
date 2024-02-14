from connect import * 

# create a subroutine to add records in the films table 

def insert_films():
    # filmID field is a primary autoincrement field, no data input is required
    # create five input statements for the title, release date, rating, duration and genre field
    filmTitle = input("Enter the title of the film: ")
    filmRelease = input("Enter the year the film was released: ")
    filmRating = input("Enter the film rating: ")
    filmDuration = input("Enter the duration of the film: ")
    filmGenre = input("Enter the genre of the film: ")

    dbCursor.execute("INSERT INTO tblFilms(title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", (filmTitle, filmRelease, filmRating, filmDuration, filmGenre))
    dbCon.commit()

    print(f"{filmTitle} has been inserted into the films table.")

if __name__ == "__main__":
    insert_films()

    # this conditional prevents this to be run automatically, instead it has to be imported, 
    # and called upon specifically for it to run 
