import json
import os
from tkinter import Menubutton


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
        json_formatted_str = json.dumps(newCharacterData, indent=2)

        print(json_formatted_str)