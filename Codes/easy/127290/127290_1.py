# https://quera.org/problemset/127290

import math

t = int(input())
final_result = []

for _ in range(t):
    n, s, a = map(int, input().split(' '))
    
    if s <= a:
        final_result.append(-1)
        continue
        
    s += (n-1) * a
    
    if s % n == 0:
        final_result.append(int((s / n) - a))
    else:
        final_result.append(-1)
        
    
print(*final_result, sep='\n')