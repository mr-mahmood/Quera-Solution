# https://quera.org/problemset/168943

import math

n,m = map(int, input().split(' '))
matrix = []

for i in range(n):
    matrix.append([i for i in map(int, input().split(' '))])

count = 0
for i in range(0,n):
    for j in range(0,m):
        
        temp = [i, j]
        neighbors = []
        
        # find neighbors in code below
        for i2 in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]: # coordinate of neighbors for temp
            
            temp2 = [temp[0] + i2[0], temp[1] + i2[1]]
            
            if temp2[0] in [-2, -1, n, n+1]  or temp2[1] in [-2, -1, m, m+1]:
                continue 
            
            neighbors.append(matrix[ temp2[0] ] [ temp2[1] ] )
            
        # check for possibility
        flag = True
        for i3 in range(len(neighbors)):
            
            for j2 in range(i3+1, len(neighbors)):
                
                for k in range(j2+1, len(neighbors)):
                    
                    sum = neighbors[i3] + neighbors[j2] + neighbors[k]
                    
                    if math.log2(sum).is_integer():
                        count += 1
                        flag = False
                        break
                    
                if flag == False:
                    break
                
            if flag == False:
                break
                    
                    
                    
                        
                        
                        
print(count)
                    
                    
            
    

# Code wirter Github: https://github.com/mr-mahmood