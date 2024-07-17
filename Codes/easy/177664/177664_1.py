# https://quera.org/problemset/177664

n = int(input()) #number of persons

for i in range(n):
    if i == 0:
        
        final = input().split(' ')
    
    else:
    
        temp = input().split(' ')
        if int(temp[1]) > int(final[1]): #check if new added person have more money than previus person with most money
            final = temp

print(final[0])
        
# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood