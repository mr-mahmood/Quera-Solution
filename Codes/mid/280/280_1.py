# https://quera.org/problemset/280

while True:
    a = int(input())
    if 1 <= a <= 150 :
        break
while True:
    b = int(input())
    if 1 <= b <= 150 :
        break
while True:
    c = int(input())
    if 1 <= c <= 150 :
        break
f_1 = (a*a) == (b*b)+(c*c)    
f_2 = (b*b) == (a*a)+(c*c)    
f_3 = (c*c) == (b*b)+(a*a)    

if f_1 or f_2 or f_3:
    print("YES")
else:
    print("NO")
    