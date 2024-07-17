# https://quera.org/problemset/49028



while True:

    n = int(input())

    if 1 <= n <= 1_000:

        break

now = -1

count = 0

for i in range(n):

    temp = int(input())

    if i == 0:

        now = temp

    else:

        if temp != now:

            now = temp

            count += 1

            

print(count)