import re

ops = []

def getOperands(inst):
    a,b = inst.split(',')
    a = int(re.sub(r"\D","",a))
    b = int(re.sub(r"\D","",b))
    return a*b

input_file = open("input","r")
for line in input_file:
    all_ops_found = re.findall("mul\(\d*,\d*\)|do\(\)|don't\(\)",line)
    ops += all_ops_found

total = 0
do_flag = 1
for op in ops:
    if op == "don't()":
        do_flag = 0
    elif op == "do()":
        do_flag = 1
    else:
        total += getOperands(op) * do_flag
        

print(total)


#mul mul mul dont [mul mul mul do[ mul mul mul dont mul]
