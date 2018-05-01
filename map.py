import os 
import yaml
import random
import math
from pyfiglet import figlet_format
from item import Item
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/maps/"

class Map():
	def __init__(self, mapDirPath, name):
		self.tileMap = {}
		self.colorMap = {}
		self.itemMap = {}
		self.map = []
		self.name = name

		mapFile = Image.open(dir_path + mapDirPath + "/map.png")
		colorFile = open(dir_path + mapDirPath + "/colors.yml", "r")
		itemsFile = open(dir_path + mapDirPath + "/items.yml", "r")
		tileFile = open(dir_path + mapDirPath + "/tiles.yml", "r")

		self.createTileMap(tileFile)
		self.loadColors(colorFile)
		self.loadItems(itemsFile)
		self.loadMap(mapFile)

	def serialize(self):
		return self

	def printName(self):
		print(figlet_format(self.name, self.font))

	def createTileMap(self, file):
		with file as stream:
			try:
				data = yaml.load(stream)
				tiles = data['tiles']
				if 'extends' in data:
					extends = data['extends']
					name = data['name']
					if not name in extends:
						self.createTileMap(open(dir_path + extends + "/tiles.yml", "r"))
						self.loadColors(open(dir_path + extends + "/colors.yml", "r"))
				if 'font' in data:
					self.font = data['font']
				for tile in tiles:
					self.tileMap[tile] = tiles[tile]
			except yaml.YAMLError as exc:
				print(exc)

	def loadColors(self, file):
		with file as stream:
			try:
				colors = yaml.load(stream)['colors']
				for key in colors:
					self.colorMap[key] = colors[key]
			except yaml.YAMLError as exc:
					print(exc)

	def loadItems(self, file):
		with file as stream:
			try:
				data = yaml.load(stream)
				items = data['items']
				if 'extends' in data:
					extends = data['extends']
					name = data['name']
					if not name in extends:
						self.loadItems(open(dir_path + extends + "/items.yml", "r"))
				for item in items:
					self.itemMap[item] = items[item]
			except yaml.YAMLError as exc:
				print(exc)

	def loadMap(self, file):
		pixels = file.load()
		width = file.size[0]
		height = file.size[1]
		for y in range(0, height):
			mapRow = []
			self.map.append(mapRow)
			for x in range(0, width):
				r, g, b, a = pixels[x,y]
				hexKey = '%02x%02x%02x' % (r, g, b)
				tile = self.colorMap[hexKey]
				tileData = self.tileMap[tile]
				desc = tileData['desc'].strip()
				icon = tileData['icon']
				collider = tileData['collider']
				mapTile = MapTile(x, y, icon, desc, collider)
				if 'items' in tileData:
					mapTile.spawnItems(tileData['items'], self.itemMap)
				mapRow.append(mapTile)
	
	def getTile(self, x, y):
		return self.map[y][x]

	def canMove(self, x, y):
		return not self.map[y][x].collider

class MapTile():
	def __init__(self, x, y, icon, desc, isCollider):
		self.icon = icon
		self.desc = desc
		self.x = x
		self.y = y
		self.collider = isCollider
		self.items = []
		self.itemCounts = {}

	def spawnItems(self, items, itemMap):
		for item in items:
			chance = math.floor(random.random() * 100)
			if (chance <= item['spawnChance']):
				count = math.floor(random.random() * item['maxCount']) + 1
				key = item['item']
				data = itemMap[key]
				for i in range(0, count):
					obj = Item(key, data['desc'])
					if key in self.itemCounts:
						self.itemCounts[key] += 1
					else:
						self.itemCounts[key] = 1
					self.items.append(obj)
	
	def listItems(self):
		if len(self.items) == 0:
			print("No items are on this tile")
			return None
		print("Items\n-=+=-")
		for data in self.itemCounts:
			print("{} x{}".format(capitalize(data), self.itemCounts[data]))

	def __str__(self):
		return "{}".format(self.desc)

def capitalize(data):
	data = str(data)
	return data[0:1].upper() + data[1:len(data)]