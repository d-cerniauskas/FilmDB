from connect import * 

dbCursor.execute(
    """ 
CREATE TABLE "tblFilms" (
	"filmID" INTEGER NOT NULL UNIQUE,
    "title" TEXT,
	"yearReleased" INTEGER,
	"rating" TEXT,
	"duration" INTEGER,
    "genre" TEXT,
	PRIMARY KEY("filmID" AUTOINCREMENT)
)"""
)