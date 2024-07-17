# https://quera.org/problemset/72882


n,m = (int(i) for i in input().split(' '))

food_1 = 0 #count * of given food(meat)
food_2 = 0 #count * of given food(meat)

for i in range(2):
    for j in range(n):
        temp = input()
        for k in temp:
            if i == 0:
                if k == '*':
                    food_1 += 1
            else:
                if k == '*':
                    food_2 += 1

            
print(f"{food_1} {food_2}")


# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood