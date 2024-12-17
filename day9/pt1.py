disk_map = [2,3,3,3,1,3,3,1,2,1,4,1,4,1,3,1,4,0,2]
block_arr = []
'''
input_file = open("input","r")
for line in input_file:
    disk_map = list(map(int,list(line[:len(line)-1])))
'''


file_id = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        block_arr += disk_map[i]*[file_id]
        file_id += 1
    else:
        block_arr += disk_map[i]*[-1]

print(block_arr)
i = 0
j = len(block_arr)-1

while i < j:
    if block_arr[i] == -1 and block_arr[j] != -1:
        block_arr[i],block_arr[j] = block_arr[j],block_arr[i]
        i += 1
        j -= 1

    if block_arr[i] != -1 and block_arr[j] != -1:
        i += 1

    if block_arr[j] == -1:
        j -= 1

print(block_arr)

checksum = 0
for i in range(len(block_arr)):
    block = block_arr[i]
    if block != -1:
        checksum += (i*block)

print(checksum)

