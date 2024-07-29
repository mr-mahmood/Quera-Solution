# https://quera.org/problemset/6192

a, b, c, d, e, f = map(int, input().split(' '))

box = [a, b]

ice = [[d, e], [d, f], [e, f], [e, d], [f, d], [f, e]] # diffrent ice rotaition

flag = False
for i in ice:
    if i[0] <= box[0] and i[1] <= box[1]:
        flag = True
        
if flag:
    print("zende mimuni")
    
else:
    print("dari mimiri")