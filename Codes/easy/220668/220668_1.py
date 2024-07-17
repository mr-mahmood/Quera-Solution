# https://quera.org/problemset/220668

def check(a, i, m, n):
    first = -1
    temp = 0
    flag = False
    for j in range(i, n):
        if a[j] == '0':
            temp += 1
            if first == -1:
                first = j
            if temp == m:
                flag = True
                break
        else:
            temp = 0
            first = -1
    return flag, first


while True:
    n, m = (int(j) for j in input().split(' '))
    if 1 <=  n <= 200 and 1 <=  m <= 200:
        break
    
cafe_net = ['0']*n
offers = [] #[[s,l],.....]

for i in range(m):
    s, l = (int(j) for j in input().split(' '))
    if 1 <= s <= n and 1 <= l <= n:
        offers.append([s,l])
        continue   
    
for i in offers:
    from_chair, number = i[0], i[1]
    flag, first = check(cafe_net, from_chair-1, number, n)
    while number > 0 and flag:
        cafe_net[first] = '1'
        first += 1
        number -= 1
    print(*cafe_net)

# Code wirter Github: https://github.com/mr-mahmood