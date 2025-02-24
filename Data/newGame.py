import json
import math


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
    professionList = []
    while not professionSet:
        print("Select a Profession Below for more info")
        print("1.) FBI Agent")
        print("2.) Special Forces")
        print("3.) Criminal")
        proAnswer = input("Please select a number...\n")
        match int(proAnswer):
            case 1:
                professionName = "FBI Agent"
                print("Suggested Base Stats : Con, Pow, Cha")
                print("Base Skill Ratings")
                print("---------------------------------")
                print("Alertness : 50 | Bureaucracy 40")
                print("Criminology : 50 | Drive : 50")
                print("Firearms : 50 | Forensics : 30")
                print("HUMINT : 60 | Law : 30 | Persuade : 50")
                print("Search : 50 | Unarmed Combat : 60")
                print("---------------------------------")
                print("One Additional Skill from below:")
                print("Accounting : 60 | Computer Science : 50")
                print("Foreign Language (Choose One) : 50")
                print("Heavy Weapon : 50 | Pharmacy 50")
            case 2:
                professionName = "Special Forces"
                print("Suggested Base Stats : Str, Con, Pow")
                print("Base Skill Ratings")
                print("---------------------------------")
                print("Alertness : 60 | Athletics : 60")
                print("Demolitions : 40 | Firearms : 60")
                print("Heavy Weapon : 50 | Melee Weapon : 50")
                print("Military Science (Land) : 60")
                print("Navigate : 50 | Stealth : 50")
                print("Survival : 50 | Swim : 50")
                print("Unarmed Combat : 60")
            case 3:
                professionName = "Criminal"
                print("Suggested Base Stats : Str, Dex")
                print("Base Skill Ratings")
                print("---------------------------------")
                print("Alertness : 50 | Criminology : 60")
                print("Dodge : 50 | Drive : 50 | Firearms : 50")
                print("Law : 40 | Melee Weapons : 40")
                print("Persuade : 50 | Stealth : 50")
                print("Unarmed Combat : 50")
                print("---------------------------------")
                print("Two Additional Skills from below:")
                print("Craft(Locksmithing) : 40 | Demolitions : 40")
                print("Disguise : 50 | Forensics : 40")
                print("Foreign Language (Choose One) : 40")
                print("HUMINT : 50 | Navigate : 50")
                print("Occult : 50 | Pharmacy : 40")
            case _:
                print("Invalid Option, try again")
        selectProfession = input("Press 1 if you want to select this profession...\n")
        if int(selectProfession) == 1:
            newCharacter["Profession"] = professionName
            professionSet = True
    match professionName:
        case "FBI Agent":
            newCharacter["Skills"]["Alertness"] = 50
            newCharacter["Skills"]["Bureaucracy"] = 40
            newCharacter["Skills"]["Criminology"] = 50
            newCharacter["Skills"]["Drive"] = 50
            newCharacter["Skills"]["Firearms"] = 50
            newCharacter["Skills"]["Forensics"] = 30
            newCharacter["Skills"]["HUMINT"] = 60
            newCharacter["Skills"]["Law"] = 30
            newCharacter["Skills"]["Persuade"] = 50
            newCharacter["Skills"]["Search"] = 50
            newCharacter["Skills"]["Unarmed Combat"] = 60
            additionalSkill = False
            while not additionalSkill:
                print("Select a skill from below:")
                print("1.) Accounting : 60")
                print("2.) Computer Science : 50")
                print("3.) Foreign Language (Choose One) : 50")
                print("4.) Heavy Weapon : 50 ")
                print("5.) Pharmacy : 50 ")
                addSkillAnswer = input("Enter number here: ")
                match int(addSkillAnswer):
                    case 1:
                        newCharacter["Skills"]["Accounting"] = 60
                        additionalSkill = True
                    case 2:
                        newCharacter["Skills"]["Computer Science"] = 50
                        additionalSkill = True
                    case 3:
                        languageAnswer = input("What is the language?")
                        newCharacter["Skills"]['Language']['Language 1']['Name'] = languageAnswer
                        newCharacter["Skills"]['Language']['Language 1']['Rating'] = 50
                        additionalSkill = True
                    case 4:
                        newCharacter["Skills"]["Unarmed Combat"] = 50
                        additionalSkill = True
                    case 5:
                        newCharacter["Skills"]["Unarmed Combat"] = 50
                        additionalSkill = True
                    case _:
                        print("Invalid Option, try again")
        case "Special Forces":
            newCharacter["Skills"]["Alertness"] = 60
            newCharacter["Skills"]["Athletics"] = 60
            newCharacter["Skills"]["Demolitions"] = 40
            newCharacter["Skills"]["Firearms"] = 60
            newCharacter["Skills"]["Heavy Weapon"] = 50
            newCharacter["Skills"]["Melee Weapon"] = 50
            newCharacter["Skills"]["Military Science"]["Type"] = "Land"
            newCharacter["Skills"]["Military Science"]["Rating"] = 60
            newCharacter["Skills"]["Navigate"] = 50
            newCharacter["Skills"]["Stealth"] = 50
            newCharacter["Skills"]["Survival"] = 50
            newCharacter["Skills"]["Swim"] = 50
            newCharacter["Skills"]["Unarmed Combat"] = 60
        case "Criminal":
            newCharacter["Skills"]["Alertness"] = 50
            newCharacter["Skills"]["Criminology"] = 60
            newCharacter["Skills"]["Dodge"] = 50
            newCharacter["Skills"]["Drive"] = 50
            newCharacter["Skills"]["Firearms"] = 50
            newCharacter["Skills"]["Law"] = 40
            newCharacter["Skills"]["Melee Weapons"] = 40
            newCharacter["Skills"]["Persuade"] = 50
            newCharacter["Skills"]["Stealth"] = 50
            newCharacter["Skills"]["Unarmed Combat"] = 50

            additionalSkill1 = False
            additionalSkillMenu = ["Craft(Locksmithing) : 40","Demolitions : 40",
                                   "Disguise : 50","Forensics : 40",
                                   "Foreign Language (Choose One) : 40","HUMINT : 50",
                                   "Navigate : 50","Occult : 50","Pharmacy : 40 "]
            while not additionalSkill1:
                print("Select your 1st skill:")
                print("1.) Craft(Locksmithing) : 40")
                print("2.) Demolitions : 40")
                print("3.) Disguise : 50 ")
                print("4.) Forensics : 40 ")
                print("5.) Foreign Language (Choose One) : 40")
                print("6.) HUMINT : 50 ")
                print("7.) Navigate : 50 ")
                print("8.) Occult : 50 ")
                print("9.) Pharmacy : 40 ")
                addSkillAnswer = input("Enter number here: ")
                match int(addSkillAnswer):
                    case 1:
                        del additionalSkillMenu[0]
                        newCharacter["Skills"]["Craft"]["Type"] = "Lockpicking"
                        newCharacter["Skills"]["Craft"]["Rating"] = 40
                        additionalSkill1 = True
                    case 2:
                        del additionalSkillMenu[1]
                        newCharacter["Skills"]["Demolitions"] = 40
                        additionalSkill1 = True
                    case 3:
                        del additionalSkillMenu[2]
                        newCharacter["Skills"]["Disguise"] = 50
                        additionalSkill1 = True
                    case 4:
                        del additionalSkillMenu[3]
                        newCharacter["Skills"]["Forensics"] = 40
                        additionalSkill1 = True
                    case 5:
                        del additionalSkillMenu[4]
                        languageAnswer = input("What is the language?")
                        newCharacter["Skills"]['Language']['Language 1']['Name'] = languageAnswer
                        newCharacter["Skills"]['Language']['Language 1']['Rating'] = 40
                        additionalSkill1 = True
                    case 6:
                        del additionalSkillMenu[5]
                        newCharacter["Skills"]["HUMINT"] = 50
                        additionalSkill1 = True
                    case 7:
                        del additionalSkillMenu[6]
                        newCharacter["Skills"]["Navigate"] = 50
                        additionalSkill1 = True
                    case 8:
                        del additionalSkillMenu[7]
                        newCharacter["Skills"]["Occult"] = 50
                        additionalSkill1 = True
                    case 9:
                        del additionalSkillMenu[8]
                        newCharacter["Skills"]["Pharmacy"] = 50
                        additionalSkill1 = True
                    case _:
                        print("Invalid Option, try again")

            additionalSkill2 = False
            while not additionalSkill2:
                print("Select your 2nd skill:")
                n = 1
                for x in additionalSkillMenu:
                    print(str(n) + ".) " + x)
                    n += 1
                addSkillAnswer = input("Enter number here: ")
                skillMenuIndex = int(addSkillAnswer)-1
                skill = additionalSkillMenu[skillMenuIndex]

                match skill:
                    case "Craft(Locksmithing) : 40":
                        newCharacter["Skills"]["Craft"]["Type"] = "Lockpicking"
                        newCharacter["Skills"]["Craft"]["Rating"] = 40
                        additionalSkill2 = True
                    case "Demolitions : 40":
                        newCharacter["Skills"]["Demolitions"] = 40
                        additionalSkill2 = True
                    case "Disguise : 50":
                        newCharacter["Skills"]["Disguise"] = 50
                        additionalSkill2 = True
                    case "Forensics : 40":
                        newCharacter["Skills"]["Forensics"] = 40
                        additionalSkill2 = True
                    case "Foreign Language (Choose One) : 40":
                        languageAnswer = input("What is the language?")
                        newCharacter["Skills"]['Language']['Language 1']['Name'] = languageAnswer
                        newCharacter["Skills"]['Language']['Language 1']['Rating'] = 40
                        additionalSkill2 = True
                    case "HUMINT : 50":
                        newCharacter["Skills"]["HUMINT"] = 50
                        additionalSkill2 = True
                    case "Navigate : 50":
                        newCharacter["Skills"]["Navigate"] = 50
                        additionalSkill2 = True
                    case "Occult : 50":
                        newCharacter["Skills"]["Occult"] = 50
                        additionalSkill2 = True
                    case "Pharmacy : 40":
                        newCharacter["Skills"]["Pharmacy"] = 50
                        additionalSkill2 = True
                    case _:
                        print("Invalid Option, try again")

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

    #TODO Skill assignment

    #Save Character
    fileName = "Characters/" + name + ".json"
    with open(fileName, mode="w", encoding="utf-8") as write_file:
        json.dump(newCharacter, write_file)

