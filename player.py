import os
from menu import Menu

activeMenu = None
creatingCharacter = True

class Player():
    def __init__(self, x, y):
        global creatingCharacter
        global activeMenu

        self.x = x
        self.y = y
        self.inventoryCount = {}
        self.inventory = []

        self.setStats()
        self.defaultCharacteristics()
        self.selectDwarf()
        self.selectWarrior()
        self.updateStats()
        self.chooseName()
        self.displayCharacterCreation()

        while creatingCharacter:
            self.updateStats()
            print(str(self))
            activeMenu.display()
            command = input("⚔️  ")
            activeMenu.execute(command)
            self.updateStats()
            clear()
        clear()

    def serialize(self):
        return self

    def move(self, x, y):
        self.x = x
        self.y = y

    def displayInventory(self):
        print("Inventory\n-=-=-=-=-=-")
        if not self.inventoryCount:
            print("Nothing in inventory")
        for item in self.inventoryCount:
            print("{} {}x".format(capitalize(item), self.inventoryCount[item]))

    def defaultCharacteristics(self):
        self.hairColor = "Black"
        self.hairStyle = "Straight"
        self.eyeColor = "Brown"
        self.facialHair = "None"
        self.facialHairColor = "None"
        self.complexion = "Olive"
        self.height = "5'11"
        self.weight = "145lbs"
        self.traits = []

    def setStats(self):
        self.classHealthBonus = 0
        self.raceHealthBonus = 0
        self.classStrengthBonus = 0
        self.raceStrengthBonus = 0
        self.classArcanePower = 0
        self.raceArcanePower = 0
        self.classArmor = 0
        self.raceArmor = 0
        self.classArcaneResist = 0
        self.raceArcaneResist = 0
        self.classDexterity = 0
        self.raceDexterity = 0
        self.classWisdom = 0
        self.raceWisdom = 0
        self.classIntelligence = 0
        self.raceIntelligence = 0
        self.classCharisma = 0
        self.raceCharisma = 0
        self.classWillpower = 0
        self.raceWillpower = 0
        self.classConstitution = 0
        self.raceConstitution = 0
        self.classPerception = 0
        self.racePerception = 0

    def updateStats(self):
        self.hitPoints = self.classHealthBonus + self.raceHealthBonus
        self.strength = self.classStrengthBonus + self.raceStrengthBonus
        self.arcanePower = self.classArcanePower + self.raceArcanePower
        self.armor = self.classArmor + self.raceArmor
        self.arcaneResist = self.classArcaneResist + self.raceArcaneResist
        self.dexterity = self.classDexterity + self.raceDexterity
        self.wisdom = self.classWisdom + self.raceWisdom
        self.intelligence = self.classIntelligence + self.raceIntelligence
        self.charisma = self.classCharisma + self.raceCharisma
        self.willpower = self.classWillpower + self.raceWillpower
        self.constitution = self.classConstitution + self.raceConstitution
        self.perception = self.classPerception + self.racePerception

    def chooseName(self):
        print("What's The Name Of Your Character?")
        self.name = input("👑  ")
        clear()

    def displayCharacterCreation(self):
        global activeMenu
        menuActions = ["Name", "Race", "Class", "Face", "Body", "Continue"]
        menuHotKeys = ["N", "R", "C", "F", "B", "OK"]
        menuCallbacks = [self.chooseName, self.displayRaceSelection, self.displayClassSelection, self.displayFaceSelection, self.displayBodySelection, self.characterOk]
        menu = Menu("Character Creation", menuActions, menuHotKeys, menuCallbacks)
        activeMenu = menu

    def displayRaceSelection(self):
        global activeMenu
        menuActions = ["Human", "Dwarf", "Elf", "Orc", "Troll", "Undead"]
        menuCallbacks = [self.selectHuman, self.selectDwarf, self.selectElf, self.selectOrc, self.selectTroll, self.selectUndead]
        menuHotKeys = ["H", "D", "E", "O", "T", "U"]
        menu = Menu("Race Selection", menuActions, menuHotKeys, menuCallbacks)
        activeMenu = menu

    def selectHuman(self):
        self.race = "Human"
        self.raceHealthBonus = 28
        self.raceStrengthBonus = 10
        self.raceArcanePower = 8
        self.raceArmor = 9
        self.raceArcaneResist = 7
        self.raceDexterity = 6
        self.raceWisdom = 4
        self.raceIntelligence = 9
        self.raceCharisma = 6
        self.raceWillpower = 4
        self.raceConstitution = 6
        self.racePerception = 5
        self.displayCharacterCreation()
    
    def selectDwarf(self):
        self.race = "Dwarf"
        self.raceHealthBonus = 29
        self.raceStrengthBonus = 11
        self.raceArcanePower = 5
        self.raceArmor = 10
        self.raceArcaneResist = 6
        self.raceDexterity = 4
        self.raceWisdom = 7
        self.raceIntelligence = 5
        self.raceCharisma = 8
        self.raceWillpower = 9
        self.raceConstitution = 8
        self.racePerception = 5
        self.displayCharacterCreation()
    
    def selectElf(self):
        self.race = "Elf"
        self.raceHealthBonus = 24
        self.raceStrengthBonus = 8
        self.raceArcanePower = 10
        self.raceArmor = 7
        self.raceArcaneResist = 10
        self.raceDexterity = 8
        self.raceWisdom = 10
        self.raceIntelligence = 13
        self.raceCharisma = 9
        self.raceWillpower = 7
        self.raceConstitution = 8
        self.racePerception = 6
        self.displayCharacterCreation()

    def selectOrc(self):
        self.race = "Orc"
        self.raceHealthBonus = 31
        self.raceStrengthBonus = 12
        self.raceArcanePower = 4
        self.raceArmor = 11
        self.raceArcaneResist = 6
        self.raceDexterity = 4
        self.raceWisdom = 6
        self.intelligence = 3
        self.raceCharisma = 2
        self.raceWillpower = 4
        self.raceConstitution = 8
        self.racePerception = 5
        self.displayCharacterCreation()

    def selectTroll(self):
        self.race = "Troll"
        self.raceHealthBonus = 26
        self.raceStrengthBonus = 8
        self.raceArcanePower = 9
        self.raceArmor = 8
        self.raceArcaneResist = 9
        self.raceDexterity = 5
        self.raceWisdom = 7
        self.raceIntelligence = 7
        self.raceCharisma = 4
        self.raceWillpower = 5
        self.raceConstitution = 6
        self.racePerception = 4
        self.displayCharacterCreation()
    
    def selectUndead(self):
        self.race = "Undead"
        self.raceHealthBonus = 23
        self.raceStrengthBonus = 9
        self.arcanePower = 8
        self.raceArmor = 14
        self.raceArcaneResist = 13
        self.raceDexterity = 7
        self.raceWisdom = 11
        self.raceIntelligence = 9
        self.raceCharisma = 1
        self.raceWillpower = 6
        self.raceConstitution = 9
        self.racePerception = 5
        self.displayCharacterCreation()

    def displayClassSelection(self):
        global activeMenu
        menuActions = ["Warrior", "Arcane Mage", "Cleric", "Thief", "Dark Mage", "Hunter"]
        menuHotKeys = ["W", "A", "C", "T", "D", "H"]
        menuCallbacks = [self.selectWarrior, self.selectArcaneMage, self.selectCleric, self.selectThief, self.selectDarkMage, self.selectHunter]
        menu = Menu("Class Selection", menuActions, menuHotKeys, menuCallbacks)
        activeMenu = menu
    
    def selectWarrior(self):
        self.classType = "Warrior"
        self.classHealthBonus = 3
        self.classStrengthBonus = 5
        self.classArcanePower = -5
        self.classArmor = 4
        self.classArcaneResist = -1
        self.classDexterity = -2
        self.classWisdom = -1
        self.classIntelligence = 1
        self.classCharisma = 3
        self.classWillpower = -1
        self.classConstitution = 3
        self.classPerception = -1
        self.displayCharacterCreation()

    def selectArcaneMage(self):
        self.classType = "Arcane Mage"
        self.classHealthBonus = -2
        self.classStrengthBonus = -2
        self.classArcanePower = 5
        self.classArmor = -2
        self.classArcaneResist = 4
        self.classDexterity = -1
        self.classWisdom = 4
        self.classIntelligence = 3
        self.classWillpower = 5
        self.classPerception = 2
        self.displayCharacterCreation()

    def selectCleric(self):
        self.classType = "Cleric"
        self.classHealthBonus = 1
        self.classStrengthBonus = -1
        self.classArcanePower = 3
        self.classArmor = 2
        self.classArcaneResist = 5
        self.classWisdom = 5
        self.classIntelligence = 4
        self.classCharisma = 3
        self.classWillpower = 3
        self.classConstitution = 2
        self.classPerception = -1
        self.displayCharacterCreation()
    
    def selectThief(self):
        self.classType = "Thief"
        self.classHealthBonus = -1
        self.classStrengthBonus = 4
        self.classArcanePower = -3
        self.classArmor = 2
        self.classArcaneResist = 1
        self.classDexterity = 4
        self.classWisdom = -2
        self.classIntelligence = 2
        self.classCharisma = 5
        self.classWillpower = 5
        self.classConstitution = 1
        self.classPerception = 5
        self.displayCharacterCreation()

    def selectDarkMage(self):
        self.classType = "Dark Mage"
        self.classHealthBonus = 2
        self.classArcanePower = 4
        self.classArmor = 1
        self.classArcaneResist = 6
        self.classWisdom = 3
        self.classIntelligence = 4
        self.classCharisma = 2
        self.classWillpower = -2
        self.classConstitution = -1
        self.classPerception = -2
        self.displayCharacterCreation()

    def selectHunter(self):
        self.classType = "Hunter"
        self.classStrengthBonus = 3
        self.displayCharacterCreation()
        self.classArmor = 3
        self.classArcaneResist = 2
        self.classDexterity = 2
        self.classIntelligence = 2
        self.classCharisma = 1
        self.classWillpower = 6
        self.classConstitution = 5
        self.classPerception = 5
        self.classArcanePower = -2

    def displayFaceSelection(self):
        global activeMenu
        menuActions = ["Hair Style", "Hair Color", "Eye Color", "Facial Hair", "Facial Hair Color"]
        menuHotKeys = ["HS", "HC", "EC", "FH", "FHC"]
        menuCallbacks = [self.chooseHairStyle, self.chooseHairColor, self.chooseEyeColor, self.chooseFacialHair, self.chooseFacialHairColor]
        menu = Menu("Class Selection", menuActions, menuHotKeys, menuCallbacks)
        activeMenu = menu

    def chooseHairStyle(self):
        print("Choose Hair Style")
        self.hairStyle = input("⚔️  ")
        self.displayCharacterCreation()
    
    def chooseHairColor(self):
        print("Choose Hair Color")
        self.hairColor = input("⚔️  ")
        self.displayCharacterCreation()
    
    def chooseEyeColor(self):
        print("Choose Eye Color")
        self.eyeColor = input("⚔️  ")
        self.displayCharacterCreation()
    
    def chooseFacialHair(self):
        print("Choose Facial Hair")
        self.facialHair = input("⚔️  ")
        self.displayCharacterCreation()

    def chooseFacialHairColor(self):
        print("Choose Facial Hair Color")
        self.facialHairColor = input("⚔️  ")
        self.displayCharacterCreation()

    def displayBodySelection(self):
        global activeMenu
        menuActions = ["Complexion", "Height", "Weight"]
        menuHotKeys = ["C", "H", "W"]
        menuCallbacks = [self.chooseComplexion, self.chooseHeight, self.chooseWeight]
        menu = Menu("Class Selection", menuActions, menuHotKeys, menuCallbacks)
        activeMenu = menu

    def chooseComplexion(self):
        print("Choose Complexion")
        self.complexion = input("⚔️  ")
        self.displayCharacterCreation()    

    def chooseHeight(self):
        print("Choose Height")
        self.height = input("⚔️  ")
        self.displayCharacterCreation()

    def chooseWeight(self):
        print("Choose Weight")
        self.weight = input("⚔️  ")
        self.displayCharacterCreation()

    def characterOk(self):
        global creatingCharacter
        creatingCharacter = False

    def strTraits(self):
        if len(self.traits) == 0:
            return "None"
        else:
            str = ""
            for trait in self.traits:
                str += trait + ", "
            return str[0: len(str) - 2]

    def __str__(self):
        return (
"-=-=-=-=-=-=-=-=-=-\nName: {}\nRace: {}\nClass: {}\n-=-=-=-=-=-=-=-=-=-\n\n"
.format(self.name, self.race, self.classType)+
"Face\n-=-=-=-=-=-=-=-=-=-\nHair Style: {}\nHair Color: {}\nEye Color: {}\nFacial Hair: {}\nFacial Hair Color: {}\n-=-=-=-=-=-=-=-=-=-\n\n"
.format(self.hairStyle, self.hairColor, self.eyeColor, self.facialHair, self.facialHairColor)+
"Body\n-=-=-=-=-=-=-=-=-=-\nComplexion: {}\nHeight (ft'in): {}\nWeight (lbs): {}\n-=-=-=-=-=-=-=-=-=-\n\n"
.format(self.complexion, self.height, self.weight)+
"Stats\n-=-=-=-=-=-=-=-=-=-\nHealth: {}\nStrength: {}\nArcane Power: {}\nArmor: {}\nArcane Resist: {}\nDexterity: {}\nWisdom: {}\nIntelligence: {}\nCharisma: {}\nWillpower: {}\nConstitution: {}\nPerception: {}\n-=-=-=-=-=-=-=-=-=-\n\n"
.format(self.hitPoints, self.strength, self.arcanePower, self.armor, self.arcaneResist, self.dexterity, self.wisdom, self.intelligence, self.charisma, self.willpower, self.constitution, self.perception)+
"Traits\n-=-=-=-=-=-=-=-=-=-\n"+
self.strTraits()+
"\n-=-=-=-=-=-=-=-=-=-\n"
                )


def clear():
    os.system('cls')
    os.system('clear')

def capitalize(data):
    data = str(data)
    return data[0:1].upper() + data[1:len(data)]