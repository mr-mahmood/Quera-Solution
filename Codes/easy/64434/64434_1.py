# https://quera.org/problemset/64434



while True:

    n, m = (int(j) for j in input().split(' '))

    if 1 <=  n <= 20 and 1 <=  m <= 20:

        break

    

a = 'X'

b = '.'

result_a = []

result_b = []

for i in range(n):

    result_a.append([a*m])

    result_b.append([b*m])



final = []    

for i in range(3):

    for j in range(3):

        if i == j or (i%2 == 0 and j%2 == 0):

            final.append(result_a)

        else:

            final.append(result_b)



for j in [0,3,6]:

    temp = []

    for l in range(n):

        for k in range(3):

            try:

                temp.append(*final[j+k][l]) 

            except:

                break

        if len(temp) != 0:

            print(*temp,sep='')

        temp = []

