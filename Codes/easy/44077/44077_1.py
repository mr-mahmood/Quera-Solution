# https://quera.org/problemset/44077

# we use the formula that is provide in link below, it calls Brahmagupta's formula
# https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%85%D9%88%D9%84_%D8%A8%D8%B1%D8%A7%D9%87%D9%85%D8%A7%DA%AF%D9%88%D9%BE%D8%AA%D8%A7

import math

a, b, c, d = map(int, input().split())

s = (a+b+c+d)/2
temp = (s-a)*(s-b)*(s-c)*(s-d)

k = math.sqrt(temp)
print(k)

# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood