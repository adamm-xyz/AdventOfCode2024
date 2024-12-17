plotmap = []
'''
plotmap= [
    ['R','R','R','R','I','I','C','C','F','F'],
    ['R','R','R','R','I','I','C','C','C','F'],
    ['V','V','R','R','R','C','C','F','F','F'],
    ['V','V','R','C','C','C','J','F','F','F'],
    ['V','V','V','V','C','J','J','C','F','E'],
    ['V','V','I','V','C','C','J','J','E','E'],
    ['V','V','I','I','I','C','J','J','E','E'],
    ['M','I','I','I','I','I','J','J','E','E'],
    ['M','I','I','I','S','I','J','E','E','E'],
    ['M','M','M','I','S','S','J','E','E','E']
]

'''
input_file = open("input","r")
for line in input_file:
    row = list(line[:len(line)-1])
    plotmap.append(row)

# I : {(5,0),(1,0)...},{(0,9),(7,9),...}
plant_region_map = {}


def dfs(cell,plant_id,region):
    m = len(plotmap)
    n = len(plotmap[0])
    x,y = cell
    if x < 0 or x >= m or y < 0 or y >= n or plotmap[x][y] != plant_id or cell in region:
        return
    else:
        region.add(cell)
        dfs((x+1,y),plant_id,region)
        dfs((x-1,y),plant_id,region)
        dfs((x,y+1),plant_id,region)
        dfs((x,y-1),plant_id,region)

def getRegionList(plant_id):
    region_list = []
    for i in range(len(plotmap)):
        for j in range(len(plotmap[0])):
            region = set()
            dfs((i,j),plant_id,region)
            if region not in region_list and region:
                region_list.append(region)
    return region_list

def getAllPlantID():
    plant_id_list = []
    for i in range(len(plotmap)):
        for j in range(len(plotmap[0])):
            if plotmap[i][j] not in plant_id_list:
                plant_id_list.append(plotmap[i][j])
    return plant_id_list

def getAdjacentPlants(plant_pos):
    m = len(plotmap)
    n = len(plotmap[0])
    plant_list = []
    x,y = plant_pos
    adj_pos_list = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    for adj in adj_pos_list:
        i,j = adj
        if i < 0 or i >= m or j < 0 or j >= n:
            plant_list.append('#')
        else:
            plant_list.append(plotmap[i][j])
    return plant_list

def getPerimeter(region):
    count = 0
    for pos in region:
        x,y = pos
        plant_id = plotmap[x][y]
        adjacent_plants = getAdjacentPlants(pos)
        for adj in adjacent_plants:
            if adj != plant_id:
                count +=1
    return count

def getSides(region):
    count = 0

    for pos in region:
        x,y = pos
        l,r,u,d = x-1,x+1,y-1,y+1

        if (x,u) not in region:
            if (r,y) not in region or (r,u) in region:
                count += 1
        if (x,d) not in region:
            if (r,y) not in region or (r,d) in region:
                count += 1
        if (l,y) not in region:
            if (x,d) not in region or (l,d) in region:
                count += 1
        if (r,y) not in region:
            if (x,d) not in region or (r,d) in region:
                count += 1

    return count

def getArea(region):
    return len(region)

def calcFencePrice():
    total = 0
    for k,v in plant_region_map.items():
        #print(k)
        for r in v:
            #print('area = ',getArea(r))
            #print('sides = ',getSides(r))
            price = getArea(r)*getSides(r)
            #print(price)
            total += price
    return total

def getPlantRegionMap():
    all_plants = getAllPlantID()
    for plant_id in all_plants:
        plant_region_map[plant_id] = getRegionList(plant_id)

getPlantRegionMap()
#r_region = plant_region_map['I'][1]
#print(getSides(r_region))
print(calcFencePrice())
