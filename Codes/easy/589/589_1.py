# https://quera.org/problemset/589
while True:

    n = int(input())

    if 1<=n<=10:

        break

sum = 1

for i in range(1,n+1):

    sum *= i

    

print(sum)