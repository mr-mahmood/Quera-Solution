# https://quera.org/problemset/10230



num = (int(i) for i in input().split(" "))



sum = 0

for i in num:

    if i == 0:

        sum = -1

        break

    else:

        sum += i



if sum == 180:

    print("Yes")

else: 

    print("No") 