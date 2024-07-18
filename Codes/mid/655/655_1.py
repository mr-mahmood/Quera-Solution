# https://quera.org/problemset/655

while True:
    n = int(input())
    if 1 <= n <= 10 :
        break  
final = []
for i in range(n):
    temp = input().split(' ')
    s = ''
    for j in temp:
        s += j[0].upper() + j[1:].lower() + ' '
    final.append(s)
    
print(*final,sep='\n')