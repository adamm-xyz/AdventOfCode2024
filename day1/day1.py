input_file = open("input","r")
list_a = []
list_b = []
for line in input_file:
    arr = line.split(' ')
    dist_a = int(arr[0])
    list_a.append(dist_a)
    dist_b = int(arr[-1])
    list_b.append(dist_b)
list_a = sorted(list_a)
list_b = sorted(list_b)
ans = 0

for a,b in zip(list_a,list_b):
    ans += abs(a-b)

print(ans)
