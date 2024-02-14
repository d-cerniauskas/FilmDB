import readrecord, createrecord, updaterecord, deleterecord, reportmenu

# create a function to read the optionsmenu.txt file 
def menu_file():
    with open("filmdbpt1/optionsmenu.txt") as filmsFile:
        # read data from the optionsmenu.txt file and save it in the menuOptions variable
        menuOptions = filmsFile.read()
    return menuOptions

# create the menu function 
def films_menu():
    option = 0 # initialise the option variable with an integer value
    optionsList = ["1","2","3","4","5","6"] # initiliased a list data structure with optionsList variable

    # initialised/assigned the variable 'menuChoices' to the menu_file()function 
    menuChoices = menu_file() 

    # create a while loop to repeat the code within the body of the while loop 
    while option not in optionsList:
        # call/invoke the menu_file()function assigned to the 'menuChoices' variable to display the menu options
        print(menuChoices)

        # re-assign the option variable to an input function to ask to enter user choice 
        option = input("Enter an option from the films main menu: ")

        #check if the user input from the option(assigned to the input function)variable
        # matches any of the menu options(menuChoices)
        match option:
            case option if option not in optionsList:
                # execute the code below
                print(f"{option} is not a valid choice! ") # option(assigned to the input function)variable: 0//7/8/9...
    return option
# print(films_menu())


def films():
    # create a boolean variable that can be toggled true/false or on/off
    mainProgram = True

    while mainProgram: #same writing while True

        # initialise the films_menu() function with mainMenu variable 
        mainMenu = films_menu()
        match mainMenu:
             # match option(assigned to the input function) = 1/2/3/4/5/6
             # match "1" == "1"
            case "1":
                # call the file then the function from that file
                createrecord.insert_films()

            case "2":
                deleterecord.delete_films()

            case "3":
                updaterecord.update_films()
            
            case "4":
                readrecord.read_films()
            
            case "5":
                reportmenu.films()
            
            case "6":
                #re-assign the value of the mainProgram variable to False
                mainProgram = False
                         
    input("Press the 'Enter' key to quit the films app")

if __name__ == "__main__":
    films()