from __future__ import print_function
from TableTop import TableTop

class Robot:
	directions = {
		0: 'NORTH',
		1: 'EAST',
		2: 'SOUTH',
		3: 'WEST',
		'NORTH': 0,
		'EAST': 1,
		'SOUTH': 2,
		'WEST': 3
	}

	# it can be used as place function
	def __init__(self, x, y, face, tableTop):
		self.x = int(x)
		self.y = int(y)
		self.face = face
		self.tableTop = tableTop

	def move(self):
		if (self.face == 'NORTH' and (int(self.x), int(self.y)) in self.tableTop.safeToNorth):
			self.y += 1
		if (self.face == 'SOUTH' and (int(self.x), int(self.y)) in self.tableTop.safeToSouth):
			self.y -= 1
		if (self.face == 'EAST' and (int(self.x), int(self.y)) in self.tableTop.safeToEast):
			self.x += 1
		if (self.face == 'WEST' and (int(self.x), int(self.y)) in self.tableTop.safeToWest):
			self.x -= 1
			
	def left(self):
		self.face = self.directions[(self.directions[self.face] + 3) % 4]

	def right(self):
		self.face = self.directions[(self.directions[self.face] + 1) % 4]
		print(self.face)

	def report(self):
		print (self.x, self.y, self.face, sep = ',')

# test
# t = TableTop(5,5)
# r = Robot(0,2,'NORTH', t)
# r.move()
# r.report()