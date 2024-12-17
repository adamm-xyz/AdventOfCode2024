stones = [125,17]
'''
input_file = open("input","r")
for line in input_file:
    stones = list(map(int,list(line.split(' '))))
'''

def transformStone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        mid = len(str_stone)//2
        left_stone = int(str_stone[:mid])
        right_stone = int(str_stone[mid:])
        return [left_stone,right_stone]
    else:
        return [stone*2024]

def blink(stones):
    new_stones = []
    for stone in stones:
        new_stones += transformStone(stone)
    return new_stones

for i in range(75):
    print(i)
    stones = blink(stones)
print(len(stones))
