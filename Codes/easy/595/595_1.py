# https://quera.org/problemset/595



while True:

    num = int(input())

    if 1 <= num <= 10 :

        break

    

final = []

for i in range(num):

    if i == 0:

        final.append([1])

        print(*final[i])

    elif i == 1:

        final.append([1,1])

        print(*final[i])

    else:

        temp = []

        n = 0

        m = 1

        for j in range(i+1):

            if j == 0 or j == i:

                temp.append(1)

            else:

                temp.append(final[i-1][n]+final[i-1][m])

                n += 1

                m += 1

        final.append(temp)

        print(*final[i])

        