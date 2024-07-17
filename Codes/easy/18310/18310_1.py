# https://quera.org/problemset/18310

s = list(input()) #circle string
p = input() #string that we want to find in s if possible

i = 0 # index for s
while i < len(s):
    
    i_temp = i
    j = 0 # index for p
    
    flag = True
    while flag:
        
        if s[i_temp] == p[j] :
            
            i_temp = (i_temp+1)%len(s) # make it ciruclar
            
            if j+1 >= len(p) and flag == True:
                
                print("Yes")
                i = len(s)
                break
            
            elif j+1 >= len(p) and flag == False:
                
                print("No")
                i = len(s)
                break
            
            else:
                
                j = j+1
            
        else:
            
            flag = False
            i += 1

if flag == False:
    print("No")          
            

# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood