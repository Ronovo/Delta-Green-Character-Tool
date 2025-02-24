from Objects import professions

specialForce = professions.Profession("Special Forces", [
    {"Name": "Alertness", "Skill": 60}, {"Name": "Athletics", "Skill": 60},
    {"Name": "Demolitions", "Skill": 40}, {"Name": "Firearms", "Skill": 60},
    {"Name": "Heavy Weapons", "Skill": 50}, {"Name": "Melee Weapons", "Skill": 50},
    {"Name": "Military Science (Land)", "Skill": 60}, {"Name": "Navigate", "Skill": 50},
    {"Name": "Stealth", "Skill": 50}, {"Name": "Survival", "Skill": 50},
    {"Name": "Swim", "Skill": 50}, {"Name": "Unarmed Combat", "Skill": 60}
], [])

fbi = professions.Profession("FBI Agent", [
    {"Name": "Alertness", "Skill": 50}, {"Name": "Bureaucracy", "Skill": 40},
    {"Name": "Firearms", "Skill": 50}, {"Name": "Forensics", "Skill": 30},
    {"Name": "HUMINT", "Skill": 60}, {"Name": "Law", "Skill": 30},
    {"Name": "Persuade", "Skill": 50}, {"Name": "Search", "Skill": 50},
    {"Name": "Unarmed Combat", "Skill": 60}],
    [
    {"Name": "Accounting", "Skill": 60}, {"Name": "Computer Science", "Skill": 50},
    {"Name": "Foreign Language (Choose One)", "Skill": 50}, {"Name": "Heavy Weapons", "Skill": 50},
    {"Name": "Pharmacy", "Skill" : 50},
    ])

criminal = professions.Profession("Criminal",[
    {"Name": "Alertness", "Skill": 50}, {"Name": "Criminology", "Skill": 60},
    {"Name": "Dodge", "Skill": 50}, {"Name": "Drive", "Skill": 50},
    {"Name": "Firearms", "Skill": 50}, {"Name": "Law", "Skill": 40},
    {"Name": "Melee Weapons", "Skill": 40}, {"Name": "Persuade", "Skill": 50},
    {"Name": "Stealth", "Skill": 50},{"Name": "Unarmed Combat", "Skill": 50}],
    [
    {"Name": "Craft(Locksmithing)", "Skill": 40}, {"Name": "Demolitions", "Skill": 40},
    {"Name": "Disguise", "Skill": 50}, {"Name": "Forensics", "Skill": 40},
    {"Name": "Foreign Language (Choose One)", "Skill": 40}, {"Name": "HUMINT", "Skill": 50},
    {"Name": "Navigate", "Skill" : 50},{"Name": "Occult", "Skill" : 50},{"Name": "Pharmacy", "Skill" : 40},
    ])