import curses
import time
mywindow = curses.initscr()

def getMatStr(mat):
    x = ''
    for row in mat:
        x += row
        x += '\n'
    return x

def getGuardPos(lab,guard_dir):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab_map[i][j] == guard_dir:
                return i,j
    print('counldnt find ' + guard_dir)

def getAdjObj(lab,pos,direction):
    i,j = pos
    if direction == '^':
        new_pos = i-1,j
    elif direction == 'v':
        new_pos = i+1,j
    elif direction == '<':
        new_pos = i,j-1
    elif direction == '>':
        new_pos = i,j+1

    if not outOfBounds(lab,new_pos):
        return lab[new_pos[0]][new_pos[1]]

def outOfBounds(lab,pos):
    if not lab:
        return True
    i,j = pos
    m = len(lab)
    n = len(lab[0])
    if i >= 0 and i < m and j >= 0 and j < n:
        return False
    return True

def travel(pos,dir_):
    i,j = pos
    if dir_ == '^':
        new_pos = i-1,j
    elif dir_ == '>':
        new_pos = i,j+1
    elif dir_ == 'v':
        new_pos = i+1,j
    elif dir_ == '<':
        new_pos = i,j-1
    return new_pos


def updateMap(lab, old_pos, new_pos, sym):
    i,j = old_pos
    row = list(lab[i])
    row[j] = '.'
    lab_map[i] = ''.join(row)

    i,j = new_pos
    row = list(lab[i])
    row[j] = sym
    lab_map[i] = ''.join(row)

    return lab

def updateLab(lab_map):
    global dir_index #0,1,2,3
    global guard_dir #<,^,v,>
    global directions 
    global guard_pos #(5,4)
    global visited

    guard_pos = getGuardPos(lab_map,guard_dir)
    visited.add(guard_pos)
    next_obj = getAdjObj(lab_map, guard_pos, guard_dir)
    if next_obj == '#':
        dir_index += 1
        guard_dir = directions[dir_index % 4]

    next_guard_pos = travel(guard_pos,guard_dir)
    if outOfBounds(lab_map, next_guard_pos):
        return
    lab_map = updateMap(lab_map, guard_pos, next_guard_pos, guard_dir)
    guard_pos = next_guard_pos

    return lab_map

lab_map = []
lab_map = [
    '....#.....',
    '.........#',
    '..........',
    '..#.......',
    '.......#..',
    '..........',
    '.#..^.....',
    '........#.',
    '#.........',
    '......#...',
]
'''
input_file = open("input","r")
for line in input_file:
    lab_map.append(line[:len(line)-1])
'''
dir_index = 0
guard_dir = '^'
directions = ['^','>','v','<']
visited = set()
guard_pos = getGuardPos(lab_map,guard_dir)
'''
while True:
    lab_map = updateLab(lab_map)
    if lab_map == None:
        print(len(visited))
        break
'''
time.sleep(3)
while True:
    lab_map = updateLab(lab_map)
    if lab_map == None:
        print(len(visited))
        time.sleep(5)
        curses.endwin()
        quit()
    mywindow.addstr(0,0, getMatStr(lab_map))
    mywindow.refresh()
    time.sleep(0.5)

curses.endwin()
quit()
