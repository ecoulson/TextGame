import os
import sys
import pickle
from world import World
from player import Player
from menu import Menu
from enum import Enum
from pyfiglet import figlet_format

class InitState(Enum):
    LOAD = 1
    NEW = 2

activeMenu = None
initState = None

def play():
    global activeMenu
    global initState
    world = None
    
    mainMenu()

    while activeMenu != None:
        char = input("⚔️  ")
        activeMenu.execute(char)

    if (initState == InitState.NEW):
        world = World()
    elif (initState == InitState.LOAD):
        fileNames = os.listdir('./saves')
        i = 0
        print("\tSave Files")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        for name in fileNames: 
            i += 1
            print("{}: {}".format(i, name.split('.')[0]))

        print("\nEnter load name")
        possibleFile = str(input("⚔️  ")).lower()

        for name in fileNames:
            if possibleFile == name.split('.')[0]:
                file = open('./saves/{}.dat'.format(possibleFile), 'rb')
                world = pickle.load(file)
                clear()
    world.start()

def mainMenu():
    global activeMenu
    clear()
    menuActions = ["Create Game", "Load Game", "Settings", "Quit"]
    menuHotKeys = [1,2,3,"Q"]
    menuCallbacks = [createGame, loadGame, settings, quit]
    menu = Menu(figlet_format("Oryx", "roman"), menuActions, menuHotKeys, menuCallbacks)
    menu.display()
    activeMenu = menu

def createGame():
    global activeMenu
    global initState
    clear()
    initState = InitState.NEW
    activeMenu = None

def loadGame():
    global activeMenu
    global initState
    clear()
    activeMenu = None
    initState = InitState.LOAD

def settings():
    global activeMenu
    clear()
    menuActions = ["Hot Keys", "Customize", "Main Menu"]
    menuHotKeys = [1, 2, "B"]
    menuCallbacks = [error, error, mainMenu]
    menu = Menu("Settings", menuActions, menuHotKeys, menuCallbacks)
    menu.display()
    activeMenu = menu

def clear():
    os.system('cls')
    os.system('clear')

def quit():
    clear()
    sys.exit()

def error():
    raise NotImplementedYetError('Specific Option Not Implemented Yet')

def capitalize(data):
    data = str(data)
    return data[0:1].upper() + data[1:len(data)]

if __name__ == "__main__":
    play()