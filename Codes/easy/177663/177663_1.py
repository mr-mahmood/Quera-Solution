# https://quera.org/problemset/177663

n, a, b, c, d = map(int, input().split(' '))

count = 0
for i in range(1, n+1):
    result = [i % a, i % b, i % c, i % d]

    if 0 in result:
        count += 1
        
print(count)
