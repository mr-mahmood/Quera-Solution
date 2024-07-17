# https://quera.org/problemset/218361

row1 = [i for i in input().split(' ')]
row2 = [i for i in input().split(' ')]

sum = 0

for i in range(len(row1)):

    if row1[i] == '1':

        if row2[i] == '1':

            sum += 1

            

print(sum)