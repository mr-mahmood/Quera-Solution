# https://quera.org/problemset/3405

final = []
while True:
    n = input()
    if n == '0':
        break
    else:
        final.append(n)
        
final.reverse()
print(*final,sep='\n')