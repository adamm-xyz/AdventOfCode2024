'''
maze = [
['#','#','#','#','#','#','#','#','#','#'],
['#','.','.','O','.','.','O','.','O','#'],
['#','.','.','.','.','.','.','O','.','#'],
['#','.','O','O','.','.','O','.','O','#'],
['#','.','.','O','@','.','.','O','.','#'],
['#','O','#','.','.','O','.','.','.','#'],
['#','O','.','.','O','.','.','O','.','#'],
['#','.','O','O','.','O','.','O','O','#'],
['#','.','.','.','.','O','.','.','.','#'],
['#','#','#','#','#','#','#','#','#','#'],
]

moves = "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
'''

maze = []
moves = []
input_file = open("input","r")
for line in input_file:
    if line[0] == '#':
        maze.append(list(line[:len(line)-1]))
    elif line != '\n':
        moves += list(line[:len(line)-1])




def getRoboPos():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '@':
                return (i,j)


def getNextPos(pos,move):
    x,y = pos
    if move == '<':
        return (x,y-1)
    elif move == '>':
        return (x,y+1)
    elif move == '^':
        return (x-1,y)
    elif move == 'v':
        return (x+1,y)

def moveBox(pos,move,spaces):
    next_x,next_y = getNextPos(pos,move)
    if maze[next_x][next_y] == '.':
        spaces.append((next_x,next_y))
        for space in reversed(spaces):
            x,y = space
            maze[x][y] = 'O'
        return True
    elif maze[next_x][next_y] == '#':
        return False
    spaces.append(pos)
    return moveBox((next_x,next_y),move,spaces)

def moveRobo(move):
    curr_robo_pos = getRoboPos()
    robo_x,robo_y = curr_robo_pos
    new_x, new_y = getNextPos(curr_robo_pos,move)
    if maze[new_x][new_y] == '.':
        #swap robo and .
        maze[robo_x][robo_y], maze[new_x][new_y] = maze[new_x][new_y], maze[robo_x][robo_y]
        return
        #do nothing
    elif maze[new_x][new_y] == 'O':
            #move those boxes
        if moveBox((new_x,new_y),move,[]):
            #put robot at new_pos, put empty at old space
            maze[new_x][new_y] = '@'
            maze[robo_x][robo_y] = '.'
            return

def getGPS():
    boxes = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'O':
                boxes.append((100*i)+j)
    return sum(boxes)

def printMaze():
    for row in maze:
        print(''.join(row))

printMaze()
#print(moves)
for move in moves:
    moveRobo(move)
printMaze()
print(getGPS())
