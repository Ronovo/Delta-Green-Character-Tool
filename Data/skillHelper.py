def setSkillsFromList(newCharacter, skillList):
    for x in skillList:
        match x["Name"]:
            case "Alertness":
                newCharacter["Skills"]["Alertness"] = x["Skill"]
            case "Athletics":
                newCharacter["Skills"]["Athletics"] = x["Skill"]
            case "Bureaucracy":
                newCharacter["Skills"]["Bureaucracy"] = x["Skill"]
            case "Craft(Locksmithing)":
                newCharacter["Skills"]["Craft"]["Type"] = "Lockpicking"
                newCharacter["Skills"]["Craft"]["Rating"] = x["Skill"]
            case "Criminology":
                newCharacter["Skills"]["Criminology"] = x["Skill"]
            case "Demolitions":
                newCharacter["Skills"]["Demolitions"] = x["Skill"]
            case "Disguise":
                newCharacter["Skills"]["Disguise"] = x["Skill"]
            case "Dodge":
                newCharacter["Skills"]["Dodge"] = x["Skill"]
            case "Drive":
                newCharacter["Skills"]["Drive"] = x["Skill"]
            case "Firearms":
                newCharacter["Skills"]["Firearms"] = x["Skill"]
            case "Foreign Language (Choose One)":
                languageAnswer = input("What language do you want to use?\n")
                newCharacter["Skills"]['Language']['Language 1']['Name'] = languageAnswer
                newCharacter["Skills"]['Language']['Language 1']['Rating'] = x["Skill"]
            case "Forensics":
                newCharacter["Skills"]["Forensics"] = x["Skill"]
            case "Heavy Weapons":
                newCharacter["Skills"]["Heavy Weapons"] = x["Skill"]
            case "HUMINT":
                newCharacter["Skills"]["HUMINT"] = x["Skill"]
            case "Law":
                newCharacter["Skills"]["Law"] = x["Skill"]
            case "Melee Weapons":
                newCharacter["Skills"]["Melee Weapons"] = x["Skill"]
            case "Military Science (Land)":
                newCharacter["Skills"]["Military Science"]["Type"] = "Land"
                newCharacter["Skills"]["Military Science"]["Rating"] = x["Skill"]
            case "Navigate":
                newCharacter["Skills"]["Navigate"] = x["Skill"]
            case "Occult":
                newCharacter["Skills"]["Occult"] = x["Skill"]
            case "Persuade":
                newCharacter["Skills"]["Persuade"] = x["Skill"]
            case "Pharmacy":
                newCharacter["Skills"]["Pharmacy"] = x["Skill"]
            case "Search":
                newCharacter["Skills"]["Search"] = x["Skill"]
            case "Stealth":
                newCharacter["Skills"]["Stealth"] = x["Skill"]
            case "Survival":
                newCharacter["Skills"]["Survival"] = x["Skill"]
            case "Swim":
                newCharacter["Skills"]["Swim"] = x["Skill"]
            case "Unarmed Combat":
                newCharacter["Skills"]["Unarmed Combat"] = x["Skill"]
    return newCharacter