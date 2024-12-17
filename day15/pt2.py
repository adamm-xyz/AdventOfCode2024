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

box_map = {}

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

def getBoxMap():
    box_id = 0
    boxmap = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '[':
                boxmap[box_id] = [(i,j)]
                boxmap[(i,j)] = box_id
            if maze[i][j] == ']':
                boxmap[box_id].append((i,j))
                boxmap[(i,j)] = box_id
                box_id += 1
    return boxmap

def moveRobo(move):
    curr_robo_pos = getRoboPos()
    robo_x,robo_y = curr_robo_pos
    new_x, new_y = getNextPos(curr_robo_pos,move)
    if maze[new_x][new_y] == '.':
        #swap robo and .
        maze[robo_x][robo_y], maze[new_x][new_y] = maze[new_x][new_y], maze[robo_x][robo_y]
        return
    elif maze[new_x][new_y] == '[' or maze[new_x][new_y] == ']':
        #move those boxes
        if moveBox(box_map[(new_x,new_y)],move):
            #put robot at new_pos, put empty at old space
            maze[new_x][new_y] = '@'
            maze[robo_x][robo_y] = '.'
            return

def getGPS():
    boxes = []
    for k,v in box_map.items():
        if type(v) == list:
            x,y = v[0]
            boxes.append((100*x)+y)
    return sum(boxes)

def printMaze(maze_map):
    for row in maze_map:
        print(''.join(row))

def transformMaze():
    new_maze = []
    for i in range(len(maze)):
        new_maze_row = []
        for j in range(len(maze[0])):
            if maze[i][j] == '#':
                new_maze_row.append('#')
                new_maze_row.append('#')
            elif maze[i][j] == 'O':
                new_maze_row.append('[')
                new_maze_row.append(']')
            elif maze[i][j] == '.':
                new_maze_row.append('.')
                new_maze_row.append('.')
            elif maze[i][j] == '@':
                new_maze_row.append('@')
                new_maze_row.append('.')
        new_maze.append(new_maze_row)
    return new_maze

def canMoveBox(box_id,move):
    pos_list = box_map[box_id]
    #printMaze(maze)
    curr_1,curr_2 = box_map[box_id]
    x_1,y_1 = curr_1
    x_2,y_2 = curr_2
    if move == '>':
        next_1 = x_1,y_1+1
        next_2 = x_2,y_2+1
    elif move == '<':
        next_1 = x_1,y_1-1
        next_2 = x_2,y_2-1
    elif move == 'v':
        next_1 = x_1+1,y_1
        next_2 = x_2+1,y_2
    elif move == '^':
        next_1 = x_1-1,y_1
        next_2 = x_2-1,y_2

    next_x,next_y = next_1
    if maze[next_x][next_y] == '#':
        return False
    next_x,next_y = next_2
    if maze[next_x][next_y] == '#':
        return False

    if next_1 in box_map and box_map[next_1] != box_id:
        if canMoveBox(box_map[next_1],move):
            pass
        else:
            return False
    if next_2 in box_map and box_map[next_2] != box_id:
        if canMoveBox(box_map[next_2],move):
            pass
        else:
            return False
    return True

def moveBox(box_id,move):
    pos_list = box_map[box_id]
    #printMaze(maze)
    curr_1,curr_2 = box_map[box_id]
    x_1,y_1 = curr_1
    x_2,y_2 = curr_2
    if move == '>':
        next_1 = x_1,y_1+1
        next_2 = x_2,y_2+1
    elif move == '<':
        next_1 = x_1,y_1-1
        next_2 = x_2,y_2-1
    elif move == 'v':
        next_1 = x_1+1,y_1
        next_2 = x_2+1,y_2
    elif move == '^':
        next_1 = x_1-1,y_1
        next_2 = x_2-1,y_2

    next_x,next_y = next_1
    if maze[next_x][next_y] == '#':
        return False
    next_x,next_y = next_2
    if maze[next_x][next_y] == '#':
        return False


    if next_1 in box_map and next_2 in box_map:
        if box_map[next_1] != box_id:
            if not canMoveBox(box_map[next_1],move):
                return False
        if box_map[next_2] != box_id:
            if not canMoveBox(box_map[next_2],move):
                return False

    if next_1 in box_map and box_map[next_1] != box_id:
        if canMoveBox(box_map[next_1],move):
            moveBox(box_map[next_1],move)
        else:
            return False
    if next_2 in box_map and box_map[next_2] != box_id:
        if canMoveBox(box_map[next_2],move):
            moveBox(box_map[next_2],move)
        else:
            return False

    del box_map[curr_1]
    del box_map[curr_2]
    del box_map[box_id]

    for pos in pos_list:
        x,y = pos
        maze[x][y] = '.'

    next_x,next_y = next_1
    maze[next_x][next_y] = '['
    next_x,next_y = next_2
    maze[next_x][next_y] = ']'

    box_map[box_id] = [next_1,next_2]
    box_map[next_1] = box_id
    box_map[next_2] = box_id
    return True


#printMaze(maze)
maze = transformMaze()
printMaze(maze)
box_map = getBoxMap()
for move in moves:
    moveRobo(move)
printMaze(maze)
print(getGPS())
