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

def isSafeWithProblemDamp(report):
    if not isSafe(report):
        #try with level removed
        for i in range(len(report)):
            if isSafe(report[0:i]+report[i+1:]):
                return True
        return False
    return True
safe_count = 0
input_file = open("input","r")
for line in input_file:
    arr = list(map(int,line.split(' ')))
    if isSafeWithProblemDamp(arr):
        safe_count += 1
print(safe_count)
