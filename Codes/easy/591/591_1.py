# https://quera.org/problemset/591
while True:

    n = int(input())

    if 3<=n<=10:

        break

for i in range(n):

    if i == 0 or i == n-1:

        print('*'*n)

    else:

        print(f"*{' '*(n-2)}*")