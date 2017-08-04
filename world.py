import sys
from player import Player
from map import Map
from colorama import init
init(strip = not sys.stdout.isatty())
from termcolor import cprint

class World():
    def __init__ (self):
        self.player = Player(1,1)
        self.loadStartMap()

    def loadStartMap(self):
        if (self.player.race.lower() == "human"):
            error()
        elif (self.player.race.lower() == "dwarf"):
            self.map = Map("The_Pit", "The Pit", "poison")
        elif (self.player.race.lower() == "elf"):
            error()
        elif (self.player.race.lower() == "troll"):
            error()
        elif (self.player.race.lower() == "orc"):
            error()
        else:
            error()

    def start(self):
        self.map.printName()
        while True:
            tile = self.map.getTile(self.player.x, self.player.y)
            print(capitalize(tile))
            command = self.getInput("Enter Command").lower()
            self.callCommand(command)
            print("")
    
    def getInput(self, str):
            print(str)
            return input("⚔️  ").lower()

    def callCommand(self, command):
        if "move" in command:
            args = command.strip().split(" ")
            self.commandMove(args)
        elif "list" in command:
            args = command.strip().split(" ")
            self.commandList(args)
        elif "take" in command:
            args = command.strip().split(" ")
            self.commandTake(args)
        else:
            print("Unrecognized Command")

    def commandMove(self, args):
        collision = False
        direction = ""
        if len(args) == 1:
            command = self.getInput("What Direction")
            collision, direction = self.move(command)
        else:
            collision, direction = self.move(args[1])
            
        direction = capitalize(direction)
        if collision:
            cprint(direction, 'red')
        else:
            print(direction)

    def commandList(self, args):
        tile = self.map.getTile(self.player.x, self.player.y)
        tile.listItems()
    
    def commandTake(self, args):
        item = ""
        count = 1
        tile = self.map.getTile(self.player.x, self.player.y)
        items = tile.items
        
        #handle args
        if len(args) == 1:
            tile.listItems()
            print("")
            item = self.getInput("What Item").lower()
            if item == "":
                print("No Item Selected")
                return None
            if not item in items:
                print("Item not found on tile")
                return None
            count = int(self.getInput("How Many"))
            if (count == ""):
                count = 1
        elif len(args) == 2:
            item = args[1].lower()
            if item == "":
                print("No Item Selected")
                return None
            if not item in items:
                print("Item not found on tile")
                return None
        else:
            item = args[1].lower()
            count = int(args[2])

        if count > items[item]:
            count = items[item]

        items[item] -= count

        if items[item] == 0:
            items.pop(item)

        if count > 1:
            item += "s"

        print("Took {} {}".format(count, item))

    def move(self, dir):
        x = self.player.x
        y = self.player.y
        if dir.startswith("n"):
            if y == 0:
                y = len(self.map.map)
            if self.map.canMove(x, y - 1):
                self.player.move(x, y - 1)
                return False, "Moved North"
            else:
                return True, self.map.getTile(x, y - 1)
        elif dir.startswith("e"):
            if x == len(self.map.map[y]) - 1:
                x = -1
            if self.map.canMove(x + 1, y):
                self.player.move(x + 1, y)
                return False, "Moved East"
            else:
                return True, self.map.getTile(x + 1, y)
        elif dir.startswith("s"):
            if y == len(self.map.map) - 1:
                y = -1
            if self.map.canMove(x, y + 1):
                self.player.move(x, y + 1)
                return False, "Moved South"
            else:
                return True, self.map.getTile(x, y + 1)
        elif dir.startswith("w"):
            if x == 0:
                x = len(self.map.map[y])
            if self.map.canMove(x - 1, y):
                self.player.move(x - 1, y)
                return False, "Moved West"
            else:
                return True, self.map.getTile(x - 1, y)
        else:
            return "Unrecognized Direction"

def error():
    raise NotImplementedError('Has Not Been Implemented Yet')

def capitalize(data):
    data = str(data)
    return data[0:1].upper() + data[1:len(data)]