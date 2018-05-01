import os
import sys
from player import Player
from map import Map
from colorama import init
init(strip = not sys.stdout.isatty())
from termcolor import cprint
import pickle

class World():
	def __init__ (self):
		self.player = Player(1,1)
		self.map = None
		self.loadStartMap()

	def loadStartMap(self):
		if (self.player.race.lower() == "human"):
			error()
		elif (self.player.race.lower() == "dwarf"):
			self.map = Map("The_Pit", "The Pit")
		elif (self.player.race.lower() == "elf"):
			error()
		elif (self.player.race.lower() == "troll"):
			error()
		elif (self.player.race.lower() == "orc"):
			error()
		else:
			error()

	def serialize(self):
		return self

	def start(self):
		self.map.printName()
		self.commandList([])
		while True:
			tile = self.map.getTile(self.player.x, self.player.y)
			cprint(capitalize(tile.desc + '\n'), 'blue')
			command = self.getInput("Enter Command").lower()
			self.callCommand(command)
			print("")
	
	def getInput(self, str):
			print(str)
			return input("⚔️  ").lower()

	def callCommand(self, command):
		args = command.strip().split(" ")
		if "move" in args[0]:
			self.commandMove(args)
		elif "look" in args[0]:
			self.commandList(args)
		elif "take" in args[0]:
			self.commandTake(args)
		elif "inventory" in args[0]:
			self.commandInventory(args)
		elif "drop" in args[0]:
			self.commandDrop(args)
		elif "help" in args[0]:
			self.commandHelp(args)
		elif "save" in args[0]:
			self.commandSave(args)
		elif "exit" in args[0]:
			self.commandSave(args)
			self.commandExit(args)
		elif "stats" in args[0]:
			self.commandStats(args)
		elif "map" in args[0]:
			self.commandMap(args)
		else:
			print("Unrecognized Command")

	def commandExit(self, args):
		print("Exiting...")
		os.system("cls")
		os.system("clear")
		sys.exit()

	def commandMap(self, args):
		self.map.printName()
		currentMap = self.map.map
		for y in range(len(currentMap)):
			line = ""
			for x in range(len(currentMap[y])):
				if x == self.player.x and y == self.player.y:
					# prints player with a green color on the map
					line = line + '\33[32m' + self.player.name[0] + '\33[0m'
				else:
					line = line + currentMap[y][x].icon
			print(line)

	def commandSave(self, args):
		print("Saving game file...")
		saveName = self.getInput("Enter save name")
		with open("saves/{}.dat".format(saveName), 'wb') as file:
			pickle.dump(self.serialize(), file, protocol=2)

	def commandStats(self, args):
		print(self.player)

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
			self.commandList([])

	def commandList(self, args):
		tile = self.map.getTile(self.player.x, self.player.y)
		tile.listItems()
	
	def commandTake(self, args):
		count = 1
		tile = self.map.getTile(self.player.x, self.player.y)
		items = tile.items
		itemCounts = tile.itemCounts
		itemStr = ""

		if len(items) == 0:
			print("No items on this tile")
			return None
		elif len(args) == 1:
			tile.listItems()
			print("")
			itemStr = self.getInput("What Item?").lower()
			count = int(self.getInput("How many?").lower())
		else:
			for i in range(1, len(args)):
				try:
					count = int(args[i].strip())
				except ValueError:
					itemStr += args[i] + " "
		itemStr = itemStr.strip()

		i = 0
		originalCount = count
		maxCount = itemCounts[itemStr]
		if originalCount > maxCount:
			originalCount = maxCount
		while i < len(items):
			if items[i].name == itemStr.strip() and count > 0:
				if items[i].name in self.player.inventoryCount:
					if self.player.inventoryCount[items[i].name] < 100:
						self.player.inventoryCount[items[i].name] += 1
					else: 
						print("You have too many {}s".format(items[i].name))
						return None
				else:
					self.player.inventoryCount[items[i].name] = 1
				self.player.inventory.append(items[i])
				itemCounts[items[i].name] -= 1
				if itemCounts[items[i].name] == 0:
					del itemCounts[items[i].name]
				items.remove(items[i])
				i -= 1
				count -= 1
			i += 1

		if originalCount > 1:
			itemStr = itemStr.strip()
			itemStr += "s"

		print("Took {} {}".format(originalCount, itemStr))

	def commandDrop(self, args): 
		count = 1
		tile = self.map.getTile(self.player.x, self.player.y)
		items = self.player.inventory
		itemCounts = self.player.inventoryCount
		itemStr = ""
		
		if len(args) == 1:
			self.player.displayInventory()
			print("")
			itemStr = self.getInput("What Item?").lower()
			count = int(self.getInput("How many?").lower())
		else:
			for i in range(1, len(args)):
				try:
					count = int(args[i].strip())
				except ValueError:
					itemStr += args[i] + " "

		i = 0
		originalCount = count
		while (i < len(items)):
			if items[i].name == itemStr.strip() and count > 0:
				if items[i].name in tile.itemCounts:
					tile.itemCounts[items[i].name] += 1
				else:
					tile.itemCounts[items[i].name] = 1
				tile.items.append(items[i])
				itemCounts[items[i].name] -=1
				if itemCounts[items[i].name] == 0:
					del itemCounts[items[i].name]
				items.remove(items[i])
				i -= 1
				count -=1
			i += 1

		if originalCount > 1:
			itemStr += "s"
		
		print("Left {} {}".format(originalCount, itemStr))

	def commandInventory(self, args):
		self.player.displayInventory()
	
	def commandHelp(self, args):
		if len(args) == 1:
			generalHelp = open('./commands/commands.txt', 'r')
			for line in generalHelp:
				data = line.split(':')
				cprint("{}: ".format(data[0].strip().lower()), 'green')
				print("{}".format(data[1].strip().lower()))
		else:
			try:
				commandHelp = open('./commands/{}.txt'.format(args[1]), 'r')
				for line in commandHelp:
					print(line[0:len(line) - 1])
			except:
				print("No extra help for command: {}".format(args[1]))
			

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