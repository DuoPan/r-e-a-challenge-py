from TableTop import TableTop
from Robot import Robot
import sys
import os

# game variables
gameStatus = {
	'INIT': 1,
	'RUNNING': 2,
}
currentStatus = gameStatus['INIT']
tableTop = TableTop(5,5)
robot = None

# core function
def run(command):
	global currentStatus
	
	if (currentStatus == gameStatus['INIT']):
		start(command)
	if (currentStatus == gameStatus['RUNNING']):
		action(command)

# initial place
def start(command):
	global currentStatus
	global robot
	
	if (command[0:5] != 'PLACE'):
		return
	location = command.split(' ')[1].split(',')
	if (isValidLocation(int(location[0]), int(location[1]))):
		robot = Robot(location[0], location[1], location[2], tableTop)
		currentStatus = gameStatus['RUNNING']

# all actions after initial place
def action(command):
	global currentStatus
	global robot

	if (command[0:5] == 'PLACE'):
		location = command.split(' ')[1].split(',')
		if (isValidLocation(int(location[0]), int(location[1]))):
			robot.place(location[0], location[1], location[2])
	elif (command == 'MOVE'):
		robot.move()
	elif (command == 'LEFT'):
		robot.left()
	elif (command == 'RIGHT'):
		robot.right()
	elif (command == 'REPORT'):
		robot.report()

# check if it is a valid place location
def isValidLocation(x, y):
	return (x in range(5) and y in range(5))

# main function
def main(f):
	while True: 
		# Get next line from file 
		line = f.readline() 
		# if line is empty, end of file is reached 
		if not line: 
			break
		# run command
		run(line.strip())
	# finish and close file
	f.close()

# read commands from text files.
if (len(sys.argv) == 1):
	f = open("testcase1.txt", "r")
	main(f)
else:
	if (os.path.isfile(sys.argv[1])):
		f = open(sys.argv[1], "r")
		main(f)
	else:
		print ('This file does not exist.')


