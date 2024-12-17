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
            prizes.append((int(x[3:])+10000000000000,int(y[3:])+10000000000000))

def findBestButtons(a_delta,b_delta,prize):
    ax,ay = a_delta
    bx,by = b_delta
    prize_x,prize_y = prize
    a_presses, r = divmod(prize_x*by - prize_y*bx, ax*by - ay*bx)
    if r:
        return None
    b_presses, r = divmod(prize_x - ax * a_presses, bx)
    if r:
        return None
    return(a_presses,b_presses)


total = 0
for i in range(len(prizes)):
    a = a_buttons[i]
    b = b_buttons[i]
    p = prizes[i]
    best_combo = findBestButtons(a,b,p)
    if best_combo:
        total += best_combo[0]*3 + best_combo[1]

print(total)

