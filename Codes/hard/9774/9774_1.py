# https://quera.org/problemset/9774

while True:
    num = input()
    if len(num) <= 100:
        break
    
final = []
for i in range(len(num)):
    final.append(num[i] + ': ' + num[i]*int(num[i]))
    
print(*final,sep='\n')