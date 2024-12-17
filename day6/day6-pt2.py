import curses
import time

def getMatStr(mat):
    x = ''
    for row in mat:
        x += row
        x += '\n'
    return x

def getGuardPos(lab,guard_dir):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab_map[i][j] in ['^','v','<','>']:
                return i,j

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
    global visitmap

    guard_pos = getGuardPos(lab_map,guard_dir)
    visited.add(guard_pos)
    if guard_pos not in visitmap:
        visitmap[guard_pos] = 0
    else:
        visitmap[guard_pos] += 1
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

lab_map_original = [
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
    lab_map_original.append(line[:len(line)-1])
'''
lab_map = lab_map_original
candidates = []
for i in range(len(lab_map)):
    for j in range(len(lab_map[0])):
        if lab_map[i][j] == '.':
            candidates.append((i,j))

#print(candidates)
dir_index = 0
guard_dir = '^'
directions = ['^','>','v','<']
guard_pos = getGuardPos(lab_map,guard_dir)
visited = set()
'''
total = 0
for can in candidates:
    i,j = can
    row = list(lab_map[i])
    row[j] = '#'
    lab_map[i] = ''.join(row)
    #print("Attempting obstacle at " + str(can))
    #print(can)

    count = len(lab_map) ** 2
    while count:
        lab_map = updateLab(lab_map)
        count -= 1
        if lab_map == None:
            break
    if lab_map != None:
        total += 1
    lab_map = lab_map_original

print(total)
'''
#print(getMatStr(lab_map))

def addNewObj(lab_map, obj_pos):
    lab_map_new = []
    for row in lab_map:
        lab_map_new.append(row)

    i,j = obj_pos
    row = list(lab_map_new[i])
    row[j] = '#'
    lab_map_new[i] = ''.join(row)
    return lab_map_new

def showMap(lab_map):
    mywindow = curses.initscr()
    if lab_map == None:
        time.sleep(2)
        curses.endwin()
        return False
    mywindow.addstr(0,0, getMatStr(lab_map))
    mywindow.refresh()
    time.sleep(0.04)
    return True

#print(candidates)
#time.sleep(1)
def printMap(lab):
    for row in lab:
        print(row)
best_obj = []

visitmap = {}

def circleCheck(visitmap):
    thresh = 10
    for k,v in visitmap.items():
        if v >= 30:
            return True
    return False
count = 0
can_max = len(candidates)
for obj in candidates:
    count += 1
    print(str(count/can_max)+'% Done')

    lab_map = addNewObj(lab_map_original, obj)
    dir_index = 0
    guard_dir = '^'
    visited = set()
    visitmap = {}
    runningInCircles = False

    while lab_map and not runningInCircles:
        lab_map = updateLab(lab_map)
        showMap(lab_map)
        runningInCircles = circleCheck(visitmap)

    if lab_map != None:
        best_obj.append(obj)

print(len(best_obj))
    
'''
for obj in candidates:
    lab_map = addNewObj(lab_map_original, obj)
    time.sleep(2)

    count = len(lab_map)**2
    while count:
        lab_map = updateLab(lab_map)
        if lab_map == None:
            count = 0
            break
        count -= 1

    if lab_map != None:
        best_obj.append(obj)
'''
