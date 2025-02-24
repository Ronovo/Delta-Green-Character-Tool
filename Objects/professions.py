class Profession:
    def __init__(self, name, skillList,secondarySkillList):
        self.name = name
        n = 1
        self.skillList = []
        for x in skillList:
            skill = {"Name": x["Name"], "Skill": x["Skill"]}
            self.skillList.append(skill)
        self.secondary = []
        for x in secondarySkillList:
            skill = {"Name": x["Name"], "Skill": x["Skill"]}
            self.secondary.append(skill)

    def displaySkillList(self):
        outputList = self.skillList
        outputMenu(outputList)

    def displaySecondarySkillList(self):
        outputList = self.secondary
        outputMenu(outputList)


def outputMenu(skillList):
    newLine = False
    outputString = ""
    comboNames = ["Military Science (Land)","Foreign Language (Choose One)","Craft(Locksmithing)"]
    for x in skillList:
        if x["Name"] in comboNames:
            if outputString != "":
                print(outputString)
            print(x["Name"] + " : " + str(x["Skill"]))
            newLine = False
        else:
            outputString = outputString + x["Name"] + " : " + str(x["Skill"])
            if not newLine:
                outputString += " | "
                newLine = True
            elif newLine:
                print(outputString)
                outputString = ""
                newLine = False