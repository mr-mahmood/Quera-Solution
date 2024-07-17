# https://quera.org/problemset/221463

def check(board, i, j, name, n, m):
    i_temp = i
    j_temp = j
    flag = False
    for i in range(2):
        if i == 0:
            c = 1     
            while i_temp-c >= 0 and j_temp-c >= 0:
                if board[i_temp-c][j_temp-c] == name:
                    flag = True
                    break
                c += 1
        if i == 1:
            c = 1     
            while i_temp+c < n  and j_temp+c < m:
                if board[i_temp+c][j_temp+c] == name:
                    flag = True
                    break
                c += 1
    return flag
def phil_north_west(board, n, m):
    for i in range(n):
        for j in range(m):
            
            flag_A = check(board, i, j, 'A', n, m)
            if flag_A == False:
                board[i][j] = 'A' 
                continue
                
            flag_B = check(board, i, j, 'B', n, m)
            if flag_B == False:
                board[i][j] = 'B'
                continue  
                 
while True:
    n , m = (int(i) for i in input().split(' '))
    if 1<= n <=100 and 1<= m <=100:
        break
board = [["." for i in range(m)]for j in range(n)]
phil_north_west(board, n, m)
for i in board:
    for j in i:
        print(j,end="")
    print()


# Code wirter Github: https://github.com/mr-mahmood