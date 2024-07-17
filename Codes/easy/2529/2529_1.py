# https://quera.org/problemset/2529
n = int(input())

names = []

for i in range(n):

    while True:

        temp = input()

        if len(temp) <= 20:

            temp = temp.lower()

            names.append(temp)

            break

result = []

for i in names:

    alpha = []

    sum_temp = 0

    for j in i:

        if j not in alpha:

            alpha.append(j)

            sum_temp += 1

    result.append(sum_temp)

    alpha = []

result.sort(reverse=True)        

print(result[0])