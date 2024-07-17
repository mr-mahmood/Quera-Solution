# https://quera.org/problemset/220669

while True:
    n = int(input())
    if 3 <= n <= 20 :
        break
result = []
a = 'D'
b = '.'
c = (2*n-2)//2
for i in range(n):
    if i == 0:
        result.append(b*c + a + b*c)
    elif i == n-1:
        s = (a+b)*c
        result.append(s[0:(2*n-2)]+a)
    else:
        result.append(b*(c-i) + a + b*(2*i-1) + a + b*(c-i))
            
for i in result:
    print(*i,sep='')

# Code wirter Github: https://github.com/mr-mahmood