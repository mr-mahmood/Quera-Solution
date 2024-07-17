# https://quera.org/problemset/132252
def smallest_two(target):

    small1 = None

    small2 = None 

    for num1 in range(1,target):

        if target % num1 == 0:

            num2 = target//num1

            if (small1 is None) or (num1+num2 < small1+small2):

                small1, small2 = num1, num2

    return small1, small2

while True:

    R, B = (int(i) for i in input().split(' '))

    if 8 <= R <= 5000 and 1 <= B <= 2000000:

        break

size = R+B

i,j = smallest_two(size)

if i > j:

    print(f"{i} {j}")

elif i < j:

    print(f"{j} {i}")

else:

    print(f"{i} {j}")