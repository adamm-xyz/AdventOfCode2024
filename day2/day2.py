def isSafe(report):
    inc = 0
    dec = 0
    for i in range(1,len(report)):
        a = report[i-1]
        b = report[i]
        diff = abs(a-b)
        if diff < 1 or diff > 3:
            return False
        if a < b:
            inc += 1
        if a > b:
            dec += 1
    if inc > 0 and dec > 0:
        return False
    return True

safe_count = 0
input_file = open("input","r")
for line in input_file:
    arr = list(map(int,line.split(' ')))
    if isSafe(arr):
        safe_count += 1
print(safe_count)
