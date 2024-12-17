rules = [
    '47|53',
    '97|13',
    '97|61',
    '97|47',
    '75|29',
    '61|13',
    '75|53',
    '29|13',
    '97|29',
    '53|29',
    '61|53',
    '97|53',
    '61|29',
    '47|13',
    '75|47',
    '97|75',
    '47|61',
    '75|61',
    '47|29',
    '75|13',
    '53|13',
]

updates = [
'75,47,61,53,29',
'97,61,53,29,13',
'75,29,13',
'75,97,47,61,53',
'61,13,29',
'97,13,75,29,47',
]
'''
rules = []
updates = []
rule_flag = True
input_file = open("input","r")
for line in input_file:
    if rule_flag and line != '\n':
        rules.append(line[:len(line)-1])
    elif not rule_flag and line != '\n':
        updates.append(line[:len(line)-1])
    if line == '\n':
        rule_flag = False
'''
def isValid(arr,rulemap):
    #1,2,3,4,5,6
    for i in range(1,len(arr)):
        page_a = arr[i-1]
        page_b = arr[i]
        if page_a not in rulemap:
            return False
        if page_b in rulemap[page_a]:
            continue
        else:
            return False
    return True

rulemap = {}

for rule in rules:
    #'47|53'
    #[47,53]
    rule = list(map(int,rule.split('|')))
    page_a,page_b = rule
    if page_a not in rulemap:
        rulemap[page_a] = [page_b]
    else:
        rulemap[page_a].append(page_b)

for k,v in rulemap.items():
    print(str(k) + ':' + str(v))

ans = 0
for update in updates:
    #'75,47,61,53,29'
    update = list(map(int,update.split(',')))
    if isValid(update,rulemap):
        ans += update[len(update)//2]

print(ans) 
