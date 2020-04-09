class TableTop:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.safeToNorth, self.safeToSouth, self.safeToWest, self.safeToEast = self.__getSafeLocations(rows, columns)

	def __getSafeLocations(self, rows, columns):
		_safeToNorth = []
		_safeToSouth = []
		_safeToWest = []
		_safeToEast = []
		for i in range(rows):
			for j in range(columns):
				# top row cannot move to north
				if (i != rows - 1):
					_safeToNorth.append((j, i))
				# bottom row cannot move to south
				if (i != 0):
					_safeToSouth.append((j, i))
				# left column cannot move to west
				if (j != 0):
					_safeToWest.append((j, i))
				# right column cannot move to east
				if (j != columns - 1):
					_safeToEast.append((j, i))
		return _safeToNorth, _safeToSouth, _safeToWest, _safeToEast

# test
# t = TableTop(1,5)
# print(t.safeToNorth)
# print(t.safeToSouth)
# print(t.safeToWest)
# print(t.safeToEast)