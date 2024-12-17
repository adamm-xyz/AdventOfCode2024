disk_map = [2,3,3,3,1,3,3,1,2,1,4,1,4,1,3,1,4,0,2]
'''
input_file = open("input","r")
for line in input_file:
    disk_map = list(map(int,list(line[:len(line)-1])))
'''
def genFullDisk(arr):
    file_id = 0
    disk = []
    for i in range(len(arr)):
        if i % 2 == 0:
            data = [file_id]*arr[i]
            file_id += 1
            disk.append(data)
        else:
            if arr[i] > 0:
                data = ['.']*arr[i]
                disk.append(data)
    return disk

def isFile(data):
    if data[0] == '.':
        return False
    return True

def getFreeSpace(arr,file):
    spaces = []
    for i in range(len(arr)):
        if arr[i][0] == '.' and i < file:
            spaces.append(arr[i])
    return spaces

def moveFile(disk,file,space):
    new_data = []
    remaining_space = []
    size_dif = len(space) - len(file)
    if size_dif >= 0:
        for i in range(len(file)):
            new_data.append(file[i])
        for i in range(size_dif):
            remaining_space.append('.')

        space_pos = disk.index(space)
        old_data_pos = disk.index(file)

        for i in range(len(disk[old_data_pos])):
            disk[old_data_pos][i] = '.'

        del disk[space_pos]
        if len(remaining_space) > 0:
            disk.insert(space_pos,remaining_space)
        disk.insert(space_pos,new_data)
        return True

    return False

def getMaxFileID(arr):
    i = len(arr)-1
    while not isFile(arr[i]):
        i -= 1
    return arr[i][0]

def moveFileToFreeSpace(arr,file):
    spaces = getFreeSpace(arr,arr.index(file))
    for space in spaces:
        if moveFile(arr,file,space):
            break
    return arr

def getFiles(arr):
    files = []
    for data in arr:
        if isFile(data):
            files.append(data)
    return files

def printDisk(arr):
    flattened = list(map(str,[x for xs in arr for x in xs]))
    print(''.join(flattened))

def defrag(arr):
    files_to_move = list(reversed(getFiles(arr)))
    for file in files_to_move:
        arr = moveFileToFreeSpace(arr,file)
        #printDisk(arr)

full_disk = genFullDisk(disk_map)
for data in full_disk:
    print(data)
#printDisk(full_disk)
#defrag(full_disk)
#printDisk(full_disk)

flattened = [x for xs in full_disk for x in xs]
checksum = 0
for i in range(len(flattened)):
    block = flattened[i]
    if block != '.': 
        checksum += (i*block)

#print(checksum)

'''
for data in full_disk:
    print(data)
'''
