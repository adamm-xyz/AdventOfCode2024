from collections import defaultdict
stones = defaultdict(int)

input_file = open("input","r")
for line in input_file:
    stones_input = list(map(int,list(line.split(' '))))

for stone in stones_input:
    stones[stone] = 1

def blink(cache,curr_stone,stone_count):
    if curr_stone == 0:
        cache[1] = cache[1] + stone_count
        return
    stone_str = str(curr_stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        cache[int(stone_str[:mid])] = cache[int(stone_str[:mid])] + stone_count
        cache[int(stone_str[mid:])] = cache[int(stone_str[mid:])] + stone_count
    else:
        cache[curr_stone*2024] = cache[curr_stone*2024] + stone_count

for i in range(75):
    cache = defaultdict(int)
    for k,v in stones.items():
        blink(cache,k,v)
    stones = cache

for k,v in stones.items():
    print('stone id ', k)
    print('stone freq ',v)
print(sum(stones.values()))
