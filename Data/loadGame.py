import json
import os


def loadSave():
    print("Load Game Called")

    cwd = os.getcwd()
    path = cwd + "/Characters"
    items = os.listdir(path)
    fileList = []
    for file in items:
        nameLength = len(file)
        cutoff = nameLength - 5
        file = file[0:cutoff]
        fileList.append(file)
    #Menu
    print("Character Menu")
    print("--------------")
    n = 1
    for option in fileList:
        print(str(n) + ".) " + option)
        n += 1
    print(str(n) + ".) Return to Main Menu\n")
    answer = input("Please choose an option\n")
    if int(answer) == n:
        return
    else:
        fileIndex = int(answer) - 1
        grabFile = fileList[fileIndex]
        newPath = path + '/' + grabFile + '.json'
        with open(newPath, mode="r", encoding="utf-8") as read_file:
            newCharacterData = json.load(read_file)
        print("------------------------")
        print("BASIC INFO")
        print("------------------------")
        print("Name : " + newCharacterData['Real Name'])
        print("Agent Name : " + newCharacterData['Agent Name'])
        print("Profession : " + newCharacterData['Profession'])
        print("Employer : " + newCharacterData['Employer'])
        print("Nationality : " + newCharacterData['Nationality'])
        print("Sex : " + newCharacterData['Nationality'] + " | DOB : " + newCharacterData['DOB'])
        print("Education : " + newCharacterData['Education'])
        print("Physical Description : " + newCharacterData['Physical Description'])
        print("Motivations : " + newCharacterData['Motivations'])
        print("------------------------")
        print("Bonds")
        print("------------------------")
        print("Bond 1 Name : " + newCharacterData['Bonds']['Bond 1']['Name'])
        print("Bond 1 Score : " + str(newCharacterData['Bonds']['Bond 1']['Score']))
        print("------------------------")
        print("BASE STATS")
        print("------------------------")
        print("Strength : " + str(newCharacterData['BaseStats']['Str']))
        print("Constitution : " + str(newCharacterData['BaseStats']['Con']))
        print("Dexterity : " + str(newCharacterData['BaseStats']['Dex']))
        print("Intelligence : " + str(newCharacterData['BaseStats']['Int']))
        print("Power : " + str(newCharacterData['BaseStats']['Pow']))
        print("Charisma : " + str(newCharacterData['BaseStats']['Cha']))
        print("------------------------")
        print("DERIVED STATS")
        print("------------------------")
        print("Hit Points : " + str(newCharacterData['DerivedStats']['HP']))
        print("Willpower : " + str(newCharacterData['DerivedStats']['WP']))
        print("Remaining Sanity : " + str(newCharacterData['DerivedStats']['San']))
        print("Breaking Point : " + str(newCharacterData['DerivedStats']['BP']))
        print("------------------------")
        print("SKILLS")
        print("------------------------")
        print("Accounting : " + str(newCharacterData['Skills']['Accounting']))
        print("Alertness : " + str(newCharacterData['Skills']['Alertness']))
        print("Anthropology : " + str(newCharacterData['Skills']['Anthropology']))
        print("Archaeology : " + str(newCharacterData['Skills']['Archaeology']))
        print("Art : " + str(newCharacterData['Skills']['Art']))
        print("Artillery : " + str(newCharacterData['Skills']['Artillery']))
        print("Athletics : " + str(newCharacterData['Skills']['Athletics']))
        print("Bureaucracy : " + str(newCharacterData['Skills']['Bureaucracy']))
        print("Computer Science : " + str(newCharacterData['Skills']['Computer Science']))
        print("Craft (" + newCharacterData['Skills']['Craft']['Type']+ "): "
              + str(newCharacterData['Skills']['Craft']['Rating']))
        print("Criminology : " + str(newCharacterData['Skills']['Criminology']))
        print("Demolitions : " + str(newCharacterData['Skills']['Demolitions']))
        print("Disguise : " + str(newCharacterData['Skills']['Disguise']))
        print("Dodge : " + str(newCharacterData['Skills']['Dodge']))
        print("Drive : " + str(newCharacterData['Skills']['Drive']))
        print("Firearms : " + str(newCharacterData['Skills']['Firearms']))
        print("First Aid : " + str(newCharacterData['Skills']['First Aid']))
        print("Forensics : " + str(newCharacterData['Skills']['Forensics']))
        print("Heavy Machinery : " + str(newCharacterData['Skills']['Heavy Machinery']))
        print("Heavy Weapons : " + str(newCharacterData['Skills']['Heavy Weapons']))
        print("History : " + str(newCharacterData['Skills']['History']))
        print("HUMINT : " + str(newCharacterData['Skills']['HumInt']))
        print("Law : " + str(newCharacterData['Skills']['Law']))
        print("Medicine : " + str(newCharacterData['Skills']['Medicine']))
        print("Melee Weapons : " + str(newCharacterData['Skills']['Melee Weapons']))
        print("Military Science(" + newCharacterData['Skills']['Military Science']['Type']
              + ") : "
              + str(newCharacterData['Skills']['Military Science']['Rating']))
        print("Navigate : " + str(newCharacterData['Skills']['Navigate']))
        print("Occult : " + str(newCharacterData['Skills']['Occult']))
        print("Persuade : " + str(newCharacterData['Skills']['Persuade']))
        print("Pharmacy : " + str(newCharacterData['Skills']['Pharmacy']))
        print("Pilot : " + str(newCharacterData['Skills']['Pilot']))
        print("Psychotherapy : " + str(newCharacterData['Skills']['Psychotherapy']))
        print("Ride : " + str(newCharacterData['Skills']['Ride']))
        print("Science : " + str(newCharacterData['Skills']['Science']))
        print("Search : " + str(newCharacterData['Skills']['Search']))
        print("SIGINT : " + str(newCharacterData['Skills']['SigInt']))
        print("Stealth : " + str(newCharacterData['Skills']['Stealth']))
        print("Surgery : " + str(newCharacterData['Skills']['Surgery']))
        print("Survival : " + str(newCharacterData['Skills']['Survival']))
        print("Swim : " + str(newCharacterData['Skills']['Swim']))
        print("Unarmed Combat : " + str(newCharacterData['Skills']['Unarmed Combat']))
        print("Unnatural : " + str(newCharacterData['Skills']['Unnatural']))
        print("------------------------")
        print("Languages coming soon")
        print("------------------------")
        input("Press Any Key To Continue...")