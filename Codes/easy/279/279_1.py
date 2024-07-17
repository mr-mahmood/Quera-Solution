# https://quera.org/problemset/279

x, a, n = map(int, input().split())
result = 0
for k in range(0,n+1):
    ii=1
    jj=1
    for i in range(k):
        ii *= n-i
        jj *= k-i
    
    result += ii//jj * pow(x,k) * pow(a,n-k)

print(result)
    
    
# Code wirter Github: https://github.com/mr-mahmood