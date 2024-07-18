# https://quera.org/problemset/10636



while True:

    n = int(input())

    if 1 <= n <= 100 :

        break

names = {}

colors = 1

for i in range(n):

    a = input().split(' ')

    if a[0] not in names:

        names[a[0]] = 1

    else:

        names[a[0]] += 1

        

a = [*names.values()]

a.sort(reverse=1)

print(a[0])