classDict = {"Warrior": ["Berserker", "Paladin", "Gunlancer"], "Gunner": ["Artillerist", "Machinist"], "Mage": ["Sorceress", "Bard", "Arcana"]}

"""class Character:
    def __init__(self, characterName, mainClass, subClass, itemLevel):
        self.characterName = characterName
        self.mainClass = mainClass
        self.subClass = subClass
        self.itemLevel = itemLevel

    def getCharacterName(self):
        return self.characterName
    
    def getMainClass(self):
        return self.mainClass
    
    def getSubClass(self):
        return self.subClass
    
    def getItemLevel(self):
        return str(self.itemLevel)
"""

"""def createCharacter():
    characterCreated = False
    classList = list(classDict.keys())
    while characterCreated != True:
        print("Available classes:\n")
        classIncr = 1
        for key in classDict.keys():
            print(str(classIncr)+ ": " + key)
            classIncr += 1
        userSelect = input("\nSelect your class: ")
        try:
            userSelect = int(userSelect)
        except ValueError:
            print("Invalid class number, please try again")
            continue
        if userSelect < 0 or userSelect > len(classDict.keys()):
            print("Invalid class number, please try again")
            continue
        else:
            userSelect -= 1
            print("You have selected " + classList[userSelect] + "\n")
            characterCreated = True"""


#createCharacter()



#testClass = Character("Daarak", classDict["Gunner"][0], 1540)

#testClass.characterInfo()