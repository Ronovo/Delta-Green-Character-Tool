import json

def createNewCharacter():

    with open("newCharacter.json", mode="r", encoding="utf-8") as read_file:
        newCharacterData = json.load(read_file)

    newCharacter = {}
    print("Welcome to the new character menu!")
    print("----------------------------------")
    print("Part 1 : General Information")
    name = input("Please enter your character's first and last name.\n")
    newCharacter = newCharacterData['New Character Template']
    newCharacter["Real Name"] = name
    fileName = "Characters/" + name + ".json"
    with open(fileName, mode="w", encoding="utf-8") as write_file:
        json.dump(newCharacter, write_file)

    print("Now it is time to pick your agent name. What codename would you like to be?")
    print("Examples would be : Agent Winters, Agent 47, Agent Red")
    agentName = input("Please enter your name, Agent ")
    newCharacter["Agent Name"] = "Agent " + agentName

    #TODO add ProfessionList
    profession = input("Please enter your profession.\n")
    newCharacter["Profession"] = profession

    #TODO add employerList
    employer = input("Please enter your employer.\n")
    newCharacter["Employer"] = employer

    nationality = input("Please enter your nationality\n")
    newCharacter["Nationality"] = nationality

    sex = input("Please provide your sex\n")
    newCharacter["Sex"] = sex

    dob = input("Please enter Date of Birth (MM/DD/YYYY)\n")
    newCharacter["DOB"] = dob

    education = input("Please insert education, if applicable\n")
    newCharacter["Education"] = education

    print("Please provide a short physical description of your character.")
    physicalDesc = input("i.e. height, weight, distinctive features...\n")
    newCharacter["Physical Description"] = physicalDesc

    fileName = "Characters/" + name + ".json"
    with open(fileName, mode="w", encoding="utf-8") as write_file:
        json.dump(newCharacter, write_file)

