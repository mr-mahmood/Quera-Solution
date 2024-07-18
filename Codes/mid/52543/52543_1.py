# https://quera.org/problemset/52543

# https://quera.org/problemset/52543

while True:
    n = int(input())
    if 1 <= n <= 100:
        break
    
temp = []
for i in input().split(' '):
    temp.append(int(i)) 
temp.sort()

for i in range(len(temp)):
    if i%2 == 0:
        print((temp[len(temp)-1]),end=' ')
        temp = temp[:len(temp)-1:]
    else:
        print((temp[0]),end=' ')
        temp = temp[1::]

        