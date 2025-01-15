# https://quera.org/problemset/31025

from math import floor
n, k = map(int, input().split())

for i in range(k):
    n = n // 2
    
print(floor(n))

# Code wirter Github: https://github.com/mr-mahmood q