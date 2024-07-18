# https://quera.org/problemset/17675

while True:
    n = int(input())
    if 1 <= n <= 100 :
        break

fibo = []
for i in range(n):
    if i in [0,1]:
        fibo.append(1)
    else:
        fibo.append(fibo[i-2]+fibo[i-1])
result = ''     
for i in range(1,n+1):
    if i in fibo:
        result += '+'
    else:
        result += '-'
        
print(result)