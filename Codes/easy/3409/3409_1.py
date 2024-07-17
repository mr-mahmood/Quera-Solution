# https://quera.org/problemset/3409

while True:

    n = int(input())

    if 1<=n<=100:

        break

       

for i in range(1, n+1):

    for j in range(1, n+1):

        print(i*j,end=' ')

    print()