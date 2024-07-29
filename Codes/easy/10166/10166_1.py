# https://quera.org/problemset/10166

keyvoon = [3, 3, 1, 1, 2, 2]
nezam = [1, 2, 3]
shir_farhad = [2, 1, 2, 3]

score = {'keyvoon': 0, 'nezam': 0, 'shir farhad': 0}

n = int(input())
answer = list(input())

for i in range(n):
    
    if int(answer[i]) == keyvoon[i % 6]:
        score['keyvoon'] += 1
        
    if int(answer[i]) == nezam[i % 3]:
        score['nezam'] += 1
        
    if int(answer[i]) == shir_farhad[i % 4]:
        score['shir farhad'] += 1



max_score = max(score.values())
print(max_score)

names = []
for i, j in score.items():
    if j == max_score:
        names.append(i)
        
names.sort()
print(*names, sep='\n')