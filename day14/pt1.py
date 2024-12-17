import curses
import time
'''
robot_data = [
    ((0,4),(3,-3)),
    ((6,3),(-1,-3)),
    ((10,3),(-1,2)),
    ((2,0),(2,-1)),
    ((0,0),(1,3)),
    ((3,0),(-2,-2)),
    ((7,6),(-1,-3)),
    ((3,0),(-1,-2)),
    ((9,3),(2,3)),
    ((7,3),(-1,2)),
    ((2,4),(2,-3)),
    ((9,5),(-3,-3)),
]
'''
def getMatStr(mat):
    x = ''
    for row in mat:
        for c in row:
            x += str(c)
        x += '\n'
    return x

def showMap(matrix):
    mywindow = curses.initscr()
    if matrix == None:
        time.sleep(2)
        curses.endwin()
        return False
    mywindow.addstr(0,0, getMatStr(matrix))
    mywindow.refresh()
    time.sleep(1.0)
    return True
robot_data = []
input_file = open("input","r")
for line in input_file:
    pos,vel = line.split(' ')
    pos = tuple(map(int,pos[2:].split(',')))
    vel = tuple(map(int,vel[2:].split(',')))
    robot_data.append((pos,vel))


robot_pos_map = {}
robot_v_map= {}
m = 103
n = 101

def genRobotData():
    robo_id = 0
    for p,v in robot_data:
        robot_pos_map[robo_id] = p
        robot_v_map[robo_id] = v
        robo_id += 1


def updateRobotPos(robo_id):
    delta = robot_v_map[robo_id]
    old_pos = robot_pos_map[robo_id]
    new_x,new_y = old_pos[0]+delta[0],old_pos[1]+delta[1]
    if new_x < 0:
        new_x += m
    if new_x >= m:
        new_x -= m
    if new_y < 0:
        new_y += n
    if new_y >= n:
        new_y -= n
    robot_pos_map[robo_id] = (new_x,new_y)

def updateAllRobots():
    for i in range(len(robot_pos_map)):
        updateRobotPos(i)

def setRobotsOnMap():
    robo_map = []
    for i in range(m):
        robo_row = []
        for j in range(n):
            robo_row.append('.')
        robo_map.append(robo_row)
    robo_id = 0

    for i in range(len(robot_pos_map)):
        x,y = robot_pos_map[i]
        if robo_map[x][y] == '.':
            robo_map[x][y] = 1
        else:
            robo_map[x][y] += 1
    return robo_map


def getSafetyFactor(robo_map):
    quad_counts = [0,0,0,0]
    mid_x = m // 2
    mid_y = n // 2
    for i in range(m):
        for j in range(n):
            if i < mid_x and j < mid_y:
                if robo_map[i][j] != '.':
                    quad_counts[0] += robo_map[i][j]
            elif i < mid_x and j > mid_y:
                if robo_map[i][j] != '.':
                    quad_counts[1] += robo_map[i][j]
            elif i > mid_x and j < mid_y:
                if robo_map[i][j] != '.':
                    quad_counts[2] += robo_map[i][j]
            elif i > mid_x and j > mid_y:
                if robo_map[i][j] != '.':
                    quad_counts[3] += robo_map[i][j]
    total = 1
    for x in quad_counts:
        total *= x
    return total


genRobotData()
for i in range(49):
    updateAllRobots()
    robmap = setRobotsOnMap()
    print(i)
showMap(robmap)

