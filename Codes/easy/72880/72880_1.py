# https://quera.org/problemset/72880

a, b, c, d, m = map(int, input().split())

if (c*m)+a > (d*m)-b:
    if c*m > d*m:
        print('Eyval baba!')
    else:
        print("Naaa, eshtebahe!")
else:
    if c*m > d*m:
        print("Naaa, eshtebahe!")
    else:
        print('Eyval baba!')
    
    

# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood