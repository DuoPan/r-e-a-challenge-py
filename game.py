from TableTop import TableTop
from Robot import Robot

# game variables
gameStatus = {
	'INIT': 1,
	'RUNNING': 2,
	'GAMEOVER': 3
}
currentStatus = gameStatus['INIT']
tableTop = TableTop(5,5)
robot = None

# main function
def run(command):
	global currentStatus
	
	if (currentStatus == gameStatus['INIT']):
		start(command)
	if (currentStatus == gameStatus['RUNNING']):
		action(command)

def start(command):
	global currentStatus
	global robot
	
	if (command[0:5] != 'PLACE'):
		return
	location = command.split(' ')[1].split(',')
	robot = Robot(location[0], location[1], location[2], tableTop)
	currentStatus = gameStatus['RUNNING']
	
def action(command):
	global currentStatus
	global robot
	
	if (command == 'MOVE'):
		robot.move()
	if (command == 'LEFT'):
		robot.left()
	if (command == 'RIGHT'):
		robot.right()
	if (command == 'REPORT'):
		robot.report()
		currentStatus = gameStatus['GAMEOVER']

# read commands from text files.
f = open("testcase1.txt", "r")

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
