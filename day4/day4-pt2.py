import re
'''
[MASXMASXMASXMAMSM]
[MASXMASXMASXMAMSM]
[XSSMAMSMXMSMAMSMX]
[XSSMAMSMXMSMAMSMX]

if A is found:
    check diag neighbors
    flatten X-MAS to a string
    if has proper amt of Ms and Ss:
        if str not MSASM or SMAMS:
            add count

M S  M S  S M  S M 
 A    A    A    A
S M  M S  M S  S M
 X    +    X    + 

only MSASM SMAMS not allowed

MMS
SAM
MSS
'''
def getDiag(i,j,mat):
    m = len(mat)
    n = len(mat[0])
    diags = []
    if i-1 >= 0 and j-1 >= 0 and i+1 < m and j+1 < n:
        #top left
        diags.append(mat[i-1][j-1])
        #top right
        diags.append(mat[i-1][j+1])
        #bot left
        diags.append(mat[i+1][j-1])
        #bot right
        diags.append(mat[i+1][j+1])
    return diags

def isXmas(arr):
    if len(arr) < 4:
        return False
    xmas_string = ''.join(arr)
    if xmas_string == 'MSSM' or xmas_string == 'SMMS':
        return False
    m_count = 0
    s_count = 0
    for c in arr:
        if c == 'M':
            m_count += 1
        if c == 'S':
            s_count += 1
    return s_count == m_count == 2


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
for i in range(len(xmas_char_mat)):
    for j in range(len(xmas_char_mat[0])):
        c = xmas_char_mat[i][j]
        if c == 'A':
            diagonal_neighbors = getDiag(i,j,xmas_char_mat)
            if isXmas(diagonal_neighbors):
                print(diagonal_neighbors)
                ans += 1
print(ans)
