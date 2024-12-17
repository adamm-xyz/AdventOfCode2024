import re
def rotateMat(matrix):
    trans = [list(row) for row in zip(*matrix)]
    for row in trans:
        row.reverse()
    return trans

def getXmasCount(arr):
    count = 0
    if len(arr) < 4:
        return 0
    for i in range(len(arr)):
        if ''.join(arr[i:i+4]) == 'XMAS' or ''.join(arr[i:i+4]) == 'SAMX':
            count += 1
    return count

def extract_diagonal_and_off_diagonal(matrix):
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Initialize an empty list to hold the results
    result = []

    # Add the bottom-left diagonal elements
    for start in range(rows - 1, -1, -1):  # Start from bottom-left
        diagonal_list = []
        r, c = start, 0
        while r < rows and c < cols:
            diagonal_list.append(matrix[r][c])
            r += 1
            c += 1
        result.append(diagonal_list)

    # Add the top-right diagonal elements
    for start in range(1, cols):  # Start from top-right
        diagonal_list = []
        r, c = 0, start
        while r < rows and c < cols:
            diagonal_list.append(matrix[r][c])
            r += 1
            c += 1
        result.append(diagonal_list)

    return result
'''
[MASXMASXMASXMAMSM]
[MASXMASXMASXMAMSM]
[XSSMAMSMXMSMAMSMX]
[XSSMAMSMXMSMAMSMX]

for horizontal and vertical,
    search each line for 'XMAS' and 'SAMX'
    rotate matrix and repeat
for diagonal?
    

 0 1 2 3
0[a,b,c,d]
1[e,f,g,h] -> [[i],[e,j],[a,f,k],[b,g,l],[c,h],[d]]
2[i,j,k,l]     [0,2],[0,1 1,2] [0,0 1,1 2,2] [1,0 2,1 3,2]

'''
xmas_char_mat = []
'''
    ['M','M','M','S','X','X','M','A','S','M'],
    ['M','S','A','M','X','M','S','M','S','A'],
    ['A','M','X','S','X','M','A','A','M','M'],
    ['M','S','A','M','A','S','M','S','M','X'],
    ['X','M','A','S','A','M','X','A','M','M'],
    ['X','X','A','M','M','X','X','A','M','A'],
    ['S','M','S','M','S','A','S','X','S','S'],
    ['S','A','X','A','M','A','S','A','A','A'],
    ['M','A','M','M','M','X','M','M','M','M'],
    ['M','X','M','X','A','X','M','A','S','X'],
]
'''
input_file = open("input","r")
for line in input_file:
    xmas_row = []
    for c in line:
        if c != '\n':
            xmas_row.append(c)
    xmas_char_mat.append(xmas_row)

ans = 0
for row in xmas_char_mat:
    ans += getXmasCount(row)
diag = extract_diagonal_and_off_diagonal(xmas_char_mat)
xmas_char_mat = rotateMat(xmas_char_mat)
diag += extract_diagonal_and_off_diagonal(xmas_char_mat)
for col in xmas_char_mat:
    ans += getXmasCount(col)
for d in diag:
    ans += getXmasCount(d)
print(ans)
