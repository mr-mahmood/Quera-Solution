# https://quera.org/problemset/226378

move = list(input())

f1 = [0,0,0,0,0,0,0,0]
f2 = [1,0,0,0,0,0,0,0]

last = 'f2'
flag = 1

for i in range(7):
    
    if move[i] == 'F':
        
        if last == 'f1':
        
            f1[i+1] = 1
            last = 'f1'
            
        elif last == 'f2':
        
            f2[i+1] = 1
            last = 'f2'
        
    elif move[i] == 'L':
        
        if last == 'f1':
            
            print("DEATH")
            flag = 0
            break
        
        elif last == 'f2':
        
            f1[i+1] = 1
            last = 'f1'
    
    elif move[i] == 'R':
        
        if last == 'f1':
        
            f2[i+1] = 1
            last = 'f2'
            
        elif last == 'f2':
        
            print("DEATH")
            flag = 0
            break

if flag == 1:      
    print(*f1, sep='')       
    print(*f2, sep='')       

# Code wirter Github: https://github.com/mr-mahmood