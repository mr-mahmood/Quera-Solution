# https://quera.org/problemset/9773



while True:

    n = int(input())

    if 1 <= n <= 19 :

        break



i = 2*n+1

ii = (n//2)+1

j = 1

for k in range(1,n+1):

    

    if ii > k:

        a = ii-k

        temp = ' '*a + '*'*j + ' '*a + ' '*a + '*'*j + ' '*a

        print(temp)

    elif k == ii:

        print('*'*n*2)

    else:

        a = k-ii

        temp = ' '*a + '*'*j + ' '*a + ' '*a + '*'*j + ' '*a

        print(temp)

    if k < ii:

        j += 2

    else:

        j -= 2

            