import json
import math
from Data import skillHelper

from Presets import professions_presets


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
    professionSet = False
    professionName = ""
    professionPreset = None
    secondaryChoices = 0
    while not professionSet:
        print("Select a Profession Below for more info")
        n = 1
        professionList = professions_presets.getProfessionList()
        for x in professionList:
            print(str(n) + ".) " + x.name)
            n += 1
        proAnswer = input("Please select a number...\n")
        selectedIndex = int(proAnswer) - 1
        professionPreset = professions_presets.searchPresetsByName(professionList[selectedIndex].name)
        professionName = professionPreset.name
        print("Options for " + professionName)
        #Make this so you search by name
        match professionPreset.name:
            case "FBI Agent":
                print("Suggested Base Stats : Con, Pow, Cha")
                print("Base Skill Ratings")
                print("---------------------------------")
                professionPreset.displaySkillList()
                print("---------------------------------")
                print("One Additional Skill from below:")
                professionPreset.displaySecondarySkillList()
                secondaryChoices = 1
            case "Special Forces":
                print("Suggested Base Stats : Str, Con, Pow")
                print("Base Skill Ratings")
                print("---------------------------------")
                professionPreset.displaySkillList()
            case "Criminal":
                print("Suggested Base Stats : Str, Dex")
                print("Base Skill Ratings")
                print("---------------------------------")
                professionPreset.displaySkillList()
                print("---------------------------------")
                print("Two Additional Skills from below:")
                professionPreset.displaySecondarySkillList()
                secondaryChoices = 2
            case _:
                print("Invalid Option, try again")
        selectProfession = input("Press 1 if you want to select this profession...\n")
        if int(selectProfession) == 1:
            newCharacter["Profession"] = professionName
            professionSet = True

    newCharacter = skillHelper.setSkillsFromList(newCharacter, professionPreset.skillList)
    if len(professionPreset.secondary) > 0:
        chosenSecondary = []
        n = secondaryChoices
        while n > 0:
            print("You have " + str(n) + " Secondary Skills to pick")
            z = 1
            for x in professionPreset.secondary:
                print(str(z) + ".) " + x["Name"] + " : " + str(x["Skill"]))
                z += 1
            secondaryAnswer = input("Please select an option...\n")
            selectIndex = int(secondaryAnswer) - 1
            chosenSecondary.append(professionPreset.secondary[selectIndex])
            del professionPreset.secondary[selectIndex]
            n -= 1
        newCharacter = skillHelper.setSkillsFromList(newCharacter,chosenSecondary)

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

    #TODO add multiple motivations
    motivation = input("What is one thing that motivates you?\n")
    newCharacter['Motivations'] = motivation

    #TODO add checks to make sure everything adds to 72
    print("----------------------------------")
    print("Part 2 : Base Statistics")
    print("There are 6 Base Stats. You have 72 points to give")
    print("Balanced Character = 12 in every Stat")
    print("Stats In order: Strength, Constitution, Dexterity, Intelligence, Power, Charisma")
    input("Are you ready to input your stats? Press anything to continue...")
    points = 72
    strength = input("Please enter your Strength(6-18) :")
    points -= int(strength)
    print("You have " + str(points) + " left")
    con = input("Please enter your Constitution(6-18) :")
    points -= int(con)
    print("You have " + str(points) + " left")
    dex = input("Please enter your Dexterity(6-18) :")
    points -= int(dex)
    print("You have " + str(points) + " left")
    intelligence = input("Please enter your Intelligence(6-18) :")
    points -= int(intelligence)
    print("You have " + str(points) + " left")
    power = input("Please enter your Power(6-18) :")
    points -= int(power)
    print("You have " + str(points) + " left")
    cha = input("Please enter your Charisma(6-18) :")

    newCharacter['BaseStats']['Str'] = int(strength)
    newCharacter['BaseStats']['Con'] = int(con)
    newCharacter['BaseStats']['Dex'] = int(dex)
    newCharacter['BaseStats']['Int'] = int(intelligence)
    newCharacter['BaseStats']['Pow'] = int(power)
    newCharacter['BaseStats']['Cha'] = int(cha)

    newCharacter['DerivedStats']['HP'] = math.ceil((newCharacter['BaseStats']['Str'] + newCharacter['BaseStats']['Con']) * 2)
    wp = newCharacter['BaseStats']['Pow']
    newCharacter['DerivedStats']['WP'] = wp
    sanity = wp * 5
    newCharacter['DerivedStats']['San'] = sanity
    breakingPoint = sanity - wp
    newCharacter['DerivedStats']['BP'] = breakingPoint

    print("HP, WP, Sanity, and BP calculated and saved to character.\n")
    print("Now that we have these stats, you need a bond.")
    print("A bond is something you can pass sanity off onto")
    print("at the cost of breaking the relationship.")
    print("It must be a person/pet/physical object, not a concept.")
    bondName = input("What would be the name of this bond?\n")
    newCharacter['Bonds']['Bond 1']['Name'] = bondName
    newCharacter['Bonds']['Bond 1']['Score'] = newCharacter['BaseStats']['Cha']

    #TODO Backgrounds

    #Save Character
    fileName = "Characters/" + name + ".json"
    with open(fileName, mode="w", encoding="utf-8") as write_file:
        json.dump(newCharacter, write_file,indent=2)

