# https://quera.org/problemset/594

after_ten = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
after_ten_2 = { 10 : 'A' , 11 : 'B' , 12 : 'C' , 13 : 'D' , 14 : 'E', 15 : 'F'}

def to_base(number, base):
    if not number:
        return [0]
    digits = []
    while number:
        temp = number % base
        digits.append(temp)
        number //= base
    return list(reversed(digits))


while True:
    a, b = (int(j) for j in input().split(' '))
    if 1 <=  a <= 100_000 and 2 <=  b <= 10:
        break

c = to_base(a, b)
c = c[::-1]
sum1 = 0
sum2 = 0
for i in range(len(c)):
    if i%2 == 0:
        sum1 += c[i]
    else:
        sum2 += c[i]

print('Yes') if sum1 == sum2 else print('No')

