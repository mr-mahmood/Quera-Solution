# https://quera.org/problemset/52542

n = int(input())
number = input().split(' ')

result = []
for i in range(n):
    if int(number[i]) > 3:
        result.append('*')
    else:
        result.append('*'*int(number[i]))
    
print(*result, sep='\n')

# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood