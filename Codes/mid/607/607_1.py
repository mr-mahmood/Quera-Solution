# https://quera.org/problemset/607

a, b, c = (int(j) for j in input().split(' '))
matrix1 = []
matrix2 = []
final = []
for i in range(a):
    temp = input().split(' ')
    matrix1.append(list(temp))
for i in range(b):
    temp = input().split(' ')
    matrix2.append(list(temp))
    
for i in range(a):
    l = []
    for j in range(c):
        temp = 0
        for k in range(b):
            temp += int(matrix1[i][k]) * int(matrix2[k][j])
        l.append(temp)
    final.append(l)
    
for i in final:
    print(*i)
    