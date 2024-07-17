# https://quera.org/problemset/171795

t = int(input()) #number of test case
result = [] #save tests result

for i in range(t):
    room, t1, t2 = (int(i) for i in input().split(' '))
    if room == 1:
        result.append(t1)
    else:
        temp = (room * t1) + ((room - 1) * t2)
        result.append(temp)

print(*result,sep='\n')

# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood