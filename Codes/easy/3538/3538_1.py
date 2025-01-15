# https://quera.org/problemset/3538

days = {
    'shanbe': 0,
    '1shanbe': 0,
    '2shanbe': 0,
    '3shanbe': 0,
    '4shanbe': 0,
    '5shanbe': 0,
    'jome': 0,
}

for i in range(3):
    number = input()
    dayss = input().split(' ')
    for day in dayss:
        if day in days.keys():
            days[day] += 1
    
count = 0
for key, value in days.items():
    if value == 0:
        count += 1
        
print(count)

# Code wirter Github: https://github.com/mr-mahmood