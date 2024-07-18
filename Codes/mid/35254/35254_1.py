# https://quera.org/problemset/35254

import math

while True:
    n = int(input())
    if 1 <= n <= 1000 :
        break  
    
m = input()

while True:
    s, t = (int(i)-1 for i in input().split(' '))
    if 0 <=  s <= n and 0 <=  t <= n:
        break
    
H_count = []

if t >= s:
    s,t = t,s
    
for i in range(t+1, s):
    temp = ''
    
    if m[i] == 'H' :
        temp += 'H'
        
        for j in range(i+1,s):
            if m[j] == 'H':
                
                temp += 'H'
                m = m[0:j:] + '.' + m[j+1::]   
                     
            else:
                break
            
        H_count.append(temp)

actions = 0

for i in H_count:
    if len(i) == 1 :
        
        actions += 1
        continue
    
    else:
        temp = ''
        while True:
            
            if len(i) == 0:
                break
            
            if math.log(len(i), 2).is_integer():
                actions += 1
                break
            
            else:
                
                temp += 'H'
                i = i[1::] 
                
        if temp != '':
            H_count.append(temp)


        
print(int(actions))
    