# https://quera.org/problemset/221462

x_position = [0, 0, 0, 0, 0, 0, 0]
y_position = [0, 0, 0, 0, 0, 0, 0]
z_position = [0, 0, 0, 0, 0, 0, 0]
for i in range(7):
    x_position[i],y_position[i],z_position[i] = (int(j) for j in input().split(' '))
    if 0 <=  x_position[i] <= 1000000 and 0 <=  y_position[i] <= 1000000 and 0 <=  z_position[i] <= 1000000:
        continue

final = [{},{},{}]
for i in range(21):
    if 0 <= i < 7:
        temp = [*final[0].keys()]
        if x_position[i] not in temp:
            final[0][x_position[i]] = 1
        else:
            final[0][x_position[i]] += 1  
                    
    elif 7 <= i < 14:
        temp = [*final[1].keys()]
        if y_position[i-7] not in temp:
            final[1][y_position[i-7]] = 1
        else:
            final[1][y_position[i-7]] += 1  
            
    elif 14 <= i < 21:
        temp = [*final[2].keys()]
        if z_position[i-14] not in temp:
            final[2][z_position[i-14]] = 1
        else:
            final[2][z_position[i-14]] += 1  
result = []
for i in final:
    for j,k in i.items():
        if k == 3 :
            result.append(j)
            break        

print(*result,sep=' ')

# Code wirter Github: https://github.com/mr-mahmood