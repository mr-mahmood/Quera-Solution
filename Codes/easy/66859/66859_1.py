# https://quera.org/problemset/66859

after_ten = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

def to_base(number, base):

    if not number:

        return [0]

    digits = []

    while number:

        digits.append(number % base)

        number //= base

    return list(reversed(digits))





while True:

    num, base = (int(j) for j in input().split(' '))

    if 1 <= num <= pow(2,31)-1 and 2 <= base <= 16:

        break

    

temp = to_base(num, base)

for i in range(len(temp)):

    if int(temp[i]) >= 10:

        for k,j in after_ten.items():

            if j == int(temp[i]):

                temp[i] = k

                break

        

print(*temp, sep='')