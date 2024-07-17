# https://quera.org/problemset/221452

while True:
    a, b = (int(j) for j in input().split(' '))
    if 0 <=  a <= 100 and 0 <=  b <= 100:
        break
print(a+b)

# Code wirter Github: https://github.com/mr-mahmood