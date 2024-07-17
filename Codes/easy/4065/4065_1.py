# https://quera.org/problemset/4065

a,b,l = (int(i) for i in input().split(" "))

sum = 0
for i in range(l):
    if i%2 == 0:
        sum += a
    else:
        sum += b
        
# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood