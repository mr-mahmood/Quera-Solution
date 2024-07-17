# https://quera.org/problemset/3540

def check(n, x, y, t):
    sum = 0
    x_move = 0
    y_move = 0
    
    if t == 0:
        x_move += 1
        n -= x
    else:
        y_move += 1
        n -= y
        
    result = 0 
    while n > 0:
        flag = True #check every time if add to sum is possible otherwise it break out of loop
        
        if n - x >= 0 and n % x == 0:
            n -= x
            x_move += 1
            flag = False
                
        if n - y >= 0 and n % y == 0:
            n -= y
            y_move += 1
            flag = False
        
        if flag == True and n > 0:
            result = -1
            break
    
    if result != -1:
        result = f"{x_move} {y_move}"
        
    return result
    
n ,x ,y = (int(i) for i in input().split(" "))

if n % x == 0:
    print(f"{n//x} 0")
    
elif n % y == 0:
    print(f"0 {n//y}")
    
else:
    temp = check(n, x, y, 0)
    if temp == -1:
        temp = check(n, x, y, 1) 
    if temp == -1:
        print(-1)
    else:
        print(temp)
    
# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood