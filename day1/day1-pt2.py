input_file = open("input","r")
list_a = []
list_b = []
for line in input_file:
    arr = line.split(' ')
    dist_a = int(arr[0])
    list_a.append(dist_a)
    dist_b = int(arr[-1])
    list_b.append(dist_b)

def getMult(x,arr):
    mult = 0
    for val in arr:
        if val == x:
            mult += 1
    return mult
#list_a = [3,4,2,1,3,3]
#list_b = [4,3,5,3,9,3]
ans = 0
for a in list_a:
    ans += a * getMult(a,list_b)

print(ans)
