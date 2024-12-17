a_buttons = []
b_buttons = []
prizes = []
input_file = open("input","r")
for line in input_file:
    if len(line) > 1:
        deltas = line.split(':')[1]
        x,y = deltas.split(',')
        if 'Button A' in line:
            a_buttons.append((int(x[3:]),int(y[3:])))
        elif 'Button B' in line:
            b_buttons.append((int(x[3:]),int(y[3:])))
        elif 'Prize' in line:
            prizes.append((int(x[3:]),int(y[3:])))

def findBestButtons(a_delta,b_delta,prize):
    memo = {}
    def dfs(x,y,mult_a,mult_b):
        if (x,y) == prize:
            return (mult_a,mult_b)
        elif x > prize[0] or y > prize[1]:
            return (float('inf'),float('inf'))
        else:
            if (x,y) in memo:
                return memo[(x,y)]
            a_dx,a_dy = x + a_delta[0], y + a_delta[1]
            b_dx,b_dy = x + b_delta[0], y + b_delta[1]
            memo[(a_dx,a_dy)] = dfs(a_dx,a_dy,mult_a+1,mult_b)
            memo[(b_dx,b_dy)] = dfs(b_dx,b_dy,mult_a,mult_b+1)
            return min(memo[(a_dx,a_dy)],memo[(b_dx,b_dy)])
    return dfs(0,0,0,0)

total = 0
for i in range(len(prizes)):
    a = a_buttons[i]
    b = b_buttons[i]
    p = prizes[i]
    best_combo = findBestButtons(a,b,p)
    if best_combo != (float('inf'),float('inf')):
        total += best_combo[0]*3 + best_combo[1]

print(total)

