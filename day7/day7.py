import itertools

equations = []
vals = []

input_file = open("input","r")
for line in input_file:
    colon_split = line.split(':')
    vals.append(colon_split[0])
    eq = []
    for x in colon_split[1].split(' '):
        if x != '':
            eq.append(int(x))
    equations.append(eq)

def getAllExpressions(nums):
    size = len(nums)
    nums = list(map(str,nums))
    #('+','+'),('+','*'),('*','+'),('*','*')...
    ops = list(itertools.product(['+','*'],repeat=size-1))
    expressions = []
    for op in ops:
        exp = []
        for pair in zip(nums,op):
            #[1,'+',2,'+',3]
            exp.extend(pair)
        exp.append(nums[-1])
        expressions.append(exp)
    return expressions

def parseExpression(exp):
    total = int(exp[0])

    for i in range(1,len(exp),2):
        op = exp[i]
        val = int(exp[i+1])

        if op == '+':
            total += val
        elif op == '*':
            total *= val

    return total


ans = 0
#[81 40 27]
#190
#print(getAllExpressions(['81','40','27']))
for eq,val in zip(equations,vals):
    expressions = getAllExpressions(eq)
    for x in expressions:
        result = parseExpression(x)
        if result == int(val):
            ans += result
            break
#print(ans)
