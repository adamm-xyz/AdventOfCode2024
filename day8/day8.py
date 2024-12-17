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
    antinode_1 = (antenna_a[0]+x, antenna_a[1]+y)
    antinode_2 = (antenna_b[0]-x, antenna_b[1]-y)
    return [antinode_1,antinode_2]

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
#0
#(1,2) (4,5) (7,0)
#A
#(7,2) (0,1)

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
    #(1,2),(4,3),(9,0) -> [(1,2),(4,3)],[(1,2),(9,0)],[(4,3),(9,0)]
    for combo in combos: 
        node_a,node_b = calcAntinode(combo[0],combo[1])
        if not outOfBounds(node_a):
            antinodes.add(node_a)
            updateMap(node_a)
        if not outOfBounds(node_b):
            antinodes.add(node_b)
            updateMap(node_b)

for row in antenna_map:
    print(row)

print(len(antinodes))
