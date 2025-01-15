# https://quera.org/problemset/178905

erfan1 = input().split(' ')
erfan2 = input().split(' ')
matin1 = input().split(' ')
matin2 = input().split(' ')

matinInDanger = 0
for i in [erfan1, erfan2]:
    for j in [matin1, matin2]:
        if i[0] == j[0] or i[1] == j[1]:
            matinInDanger += 1
            break

if matinInDanger == 1:
    print('happy')
else:
    print('unhappy')
        


