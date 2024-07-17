# https://quera.org/problemset/618

while True:

    n = int(input())

    if 1 <= n <= 10:

        break

i = 2*n+1

ii = n+1

j = 1

for k in range(1,i+1):

    if ii > k:

        a = ii-k

        print(' '*a + '*'*j)

    elif k == ii:

        print('*'*i)

    else:

        a = k-ii

        print(' '*a + '*'*j)

    if k < ii:

        j += 2

    else:

        j -= 2

        