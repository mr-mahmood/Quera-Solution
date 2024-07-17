# https://quera.org/problemset/66864



number = ''

i = 1

while len(number) < 4000:

    number += str(i)

    i += 1



while True:

    num = int(input())

    if 1 <= num <= 4000 :

        break

   

print(number[num-1])