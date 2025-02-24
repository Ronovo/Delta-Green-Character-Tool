from Data import loadGame
from Data import newGame

while 1:
    print("Welcome to Ronovo's Delta Green Charcter API")
    print("--------------------------------------------")
    print("Main Menu")
    print("---------")
    print("1. Create New Character")
    print("2. Load Character")
    print("3. Quit")
    answer = input("Please select an option...\n")
    match int(answer):
        case 1:
            newGame.createNewCharacter()
        case 2:
            loadGame.loadSave()
        case 3:
            print("Thank you for checking out my API! :)")
            input("Press any key to quit...")
            quit()
        case _:
            print ("Invalid Option. Please try again")