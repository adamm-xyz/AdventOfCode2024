from itertools import combinations

antenna_map = [
'............',
'........0...',
'.....0......',
'.......0....',
'....0.......',
'......A.....',
'............',
'............',
'........A...',
'.........A..',
'............',
'............',
]
'''


input_file = open("input","r")
for line in input_file:
    antenna_map.append(line[:len(line)-1])
'''
def calcAntinode(antenna_a, antenna_b):
    x,y = antenna_a[0]-antenna_b[0],antenna_a[1]-antenna_b[1]
    antinodes = []

    antinode_1 = antenna_a
    antinode_2 = antenna_b

    antinodes.append(antinode_1)
    antinodes.append(antinode_2)

    while not outOfBounds(antinode_1):
        antinode_1 = (antinode_1[0]+x,antinode_1[1]+y)
        antinodes.append(antinode_1)

    while not outOfBounds(antinode_2):
        antinode_2 = (antinode_2[0]-x,antinode_2[1]-y)
        antinodes.append(antinode_2)

    return antinodes

def outOfBounds(cell):
    x,y = cell
    m = len(antenna_map)
    n = len(antenna_map[0])
    if x >= 0 and x < m and y >= 0 and y < n:
        return False
    return True

def updateMap(node):
    i,j = node
    if antenna_map[i][j] == '.':
        temp = list(antenna_map[i])
        temp[j] = '#'
        antenna_map[i] = ''.join(temp)

freqmap = {}

for i in range(len(antenna_map)):
    for j in range(len(antenna_map[0])):
        freq = antenna_map[i][j]
        if freq != '.':
            if freq not in freqmap:
                freqmap[freq] = [(i,j)]
            else:
                freqmap[freq].append((i,j))

antinodes = set()
for k,v in freqmap.items():
    combos = list(combinations(v,2))
    for combo in combos:
        nodes = calcAntinode(combo[0],combo[1])
        for node in nodes:
            if not outOfBounds(node):
                antinodes.add(node)
                updateMap(node)

for row in antenna_map:
    print(row)

print(len(antinodes))
