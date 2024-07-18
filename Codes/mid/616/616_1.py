# https://quera.org/problemset/616

import math

#get input
n = int(input())

# find floor of number
a = math.floor(math.log2(n)) + 1

result = pow(2,a)
print(result)