# https://quera.org/problemset/51865



while True:

    x = int(input())

    n = int(input())

    if 0 <=  x <= 20 and 0 <=  n <= 100:

        break

    

if n == 0:

    print(20)

elif n == 7:

    print(x)

else:

    for i in range(n):

        x -= 1

        if x <= 0:

            print(0)

            break

    if x > 0:

        print(x)