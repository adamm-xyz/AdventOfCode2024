import re

prod = []

def getOperands(inst):
    a,b = inst.split(',')
    a = int(re.sub(r"\D","",a))
    b = int(re.sub(r"\D","",b))
    return a*b

input_file = open("input","r")
for line in input_file:
    mult_instrutions = re.findall("mul\(\d*,\d*\)",line)
    for instruction in mult_instrutions:
        prod.append(getOperands(instruction))

print(sum(prod))
