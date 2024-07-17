# https://quera.org/problemset/3407



while True:

    n, m = (int(i) for i in input().split(' '))

    if n in range(0, 101) and m in range(0, 101):

        break

    

board = [] 

for i in range(n):

    temp = []

    for j in range(m):

        temp.append(0)

    board.append(temp)

    

while True:

    k = int(input())

    if k in range(0, n*m+1):

        break

    

for k in range(k):

    i, j = (int(ii) for ii in input().split(' '))

    i, j = i-1, j-1

    temp = [[i-1, j], [i+1, j], [i-1, j-1], [i+1, j+1], [i-1, j+1], [i+1, j-1], [i, j-1], [i, j+1]]

    board[i][j] = '*' 

    for i in temp:

        if 0 <= i[0] < n and 0 <= i[1] < m:

            if board[i[0]][i[1]] != '*':

                board[i[0]][i[1]] += 1

    



for i in board:

    print(*i, sep=' ')