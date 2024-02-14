from connect import *
 
#create a subroutine to update records in the films table
def update_films():
    #Fields: title, yearReleased, rating, duration and genre
    # (37, 'Inception', '2010', '12A', '148', 'Action')
    # Use the primary key to update a record
    idField = input("Enter the filmID of the record to be updated: ")
 
    #  # ask for the field values to be updated: title, yearReleased, rating, duration and genre
    titleValue = input("Enter the film title: ")
    releaseValue = input("Enter the year in which the film was released: ")
    ratingValue = input("Enter the rating of the film: ")
    durationValue = input("Enter the duration of the film: ")
    genreValue = input("Enter genre of the film: ")
 
        # add single quotes to match the value as it is, in the table in the db
    titleValue  = "'"+titleValue +"'"
    releaseValue = "'"+releaseValue+"'"
    ratingValue = "'"+ratingValue+"'"
    durationValue = "'"+durationValue+"'"
    genreValue  = "'"+genreValue+"'"
 
    # update the record in the table using the idField value
    "UPDATE tblFilms SET title/yearReleased/rating/duration/genre = title value/yearReleased value/rating value/duration value/genre value"
    dbCursor.execute(f"UPDATE tblFilms SET title = {titleValue}, yearReleased = {releaseValue}, rating = {ratingValue}, duration = {durationValue}, genre = {genreValue} WHERE filmID ={idField}")
    dbCon.commit() # Makes the change/update permanent in the table
 
    print(f"Record {idField} updated in the films table")
 
if __name__ == "__main__":
    update_films()

# this is how you change all the values for a given SongID