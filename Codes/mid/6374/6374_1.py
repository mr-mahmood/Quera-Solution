# https://quera.org/problemset/6374

after_ten = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
after_ten_2 = { 10 : 'A' , 11 : 'B' , 12 : 'C' , 13 : 'D' , 14 : 'E', 15 : 'F'}

def to_dec(number, base):
    digit = []
    for i in number:
        if i.upper() in after_ten.keys():
            digit.append(after_ten[i.upper()])
        else:
            digit.append(int(i))
    digit = digit[::-1]
    count = 0
    final = 0
    for i in digit:
        final += i * pow(base, count)
        count += 1
    return to_base(final+1, 16)

def to_base(number, base):
    if not number:
        return [0]
    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return list(reversed(digits))

a = to_dec(input(), 16)
f = []
for i in a:
    if int(i) >= 10:
        f.append(after_ten_2[int(i)])
    else:
        f.append(int(i))
                
print(*f,sep='')