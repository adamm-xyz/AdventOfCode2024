#topo_map = []
topo_map = [
[8,9,0,1,0,1,2,3],
[7,8,1,2,1,8,7,4],
[8,7,4,3,0,9,6,5],
[9,6,5,4,9,8,7,4],
[4,5,6,7,8,9,0,3],
[3,2,0,1,9,0,1,2],
[0,1,3,2,9,8,0,1],
[1,0,4,5,6,7,3,2]
]

'''
input_file = open("input","r")
for line in input_file:
    topo_line = list(map(int,line[:len(line)-1]))
    topo_map.append(topo_line)
'''

def getTrailHeads(mat):
    heads = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                heads.append((i,j))
    return heads

def getTrailEnds(mat):
    heads = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 9:
                heads.append((i,j))
    return heads

def outOfBounds(pos):
    m = len(topo_map)
    n = len(topo_map[0])
    x,y = pos
    if x >= 0 and x < m and y >= 0 and y < n:
        return False
    return True

def getNextSteps(pos,curr):
    steps = []
    x,y = pos
    next_steps = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
    for step in next_steps:
        if not outOfBounds(step):
            i,j = step
            if topo_map[i][j]-1 == curr:
                steps.append(step)
    return steps

trail_heads = getTrailHeads(topo_map)
trail_ends = getTrailEnds(topo_map)
visited = set()

def searchMap(pos):
    x,y = pos
    count = 0
    steps = getNextSteps(pos,topo_map[x][y])

    for step in steps:
        if step in trail_ends and step not in visited:
            count += 1
            visited.add(step)
        else:
            count += searchMap(step)

    return count

total = 0
for head in trail_heads:
    visited = set()
    total += searchMap(head)
print(total)
