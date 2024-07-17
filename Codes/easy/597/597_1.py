# https://quera.org/problemset/597



while True:

    num = int(input())

    if 1 <= num <= 1000000 :

        break



s = 1

position = [0,0]

count = 1

for i in range(num+1):

    if count == num:

        break

    j = i % 4

    if j == 0:

        position[0] += s

        count += 1

    elif j == 1:

        position[1] += s

        count += 1

    elif j == 2:

        position[0] -= s

        count += 1

    elif j == 3:

        position[1] -= s

        count += 1

    if i % 2 == 1:

        s += 1

        

print(*position)