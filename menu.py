class Menu():
    def __init__(self, title, names, hotkeys, callbacks):
        self.title = title
        self.actions = []
        self.keyMap = {}
        self.createActions(names, hotkeys, callbacks)

    def createAction(self, actionName, hotkey, callback):
        key = str(hotkey).lower()
        self.keyMap[key] = callback
        self.keyMap[str(actionName).lower()] = callback
        action = MenuAction(actionName, hotkey, callback)
        self.actions.append(action)

    def createActions(self, actionNames, hotkeys, callbacks):
        for i in range(0, len(actionNames)):
            self.createAction(actionNames[i], hotkeys[i], callbacks[i])
    
    def display(self):
        print(str(self))
    
    def keyExists(self, keyPressed):
        return keyPressed in self.keyMap.keys()

    def execute(self, key):
        key = str(key).lower()
        if (self.keyExists(key)):
            self.keyMap[key]()
        else:
            print("Unreconginzed Key Input of [", key, "]")

    def __str__(self):
        string = "{}\n\n".format(self.title)
        for action in self.actions:
            string += str(action) + "\n"
        return string

class MenuAction():
    def __init__(self, actionName, hotkey, callback):
        self.name = actionName
        self.callback = callback
        self.hotkey = hotkey
    
    def __str__(self):
        return "[{}] {}".format(self.hotkey, self.name)
