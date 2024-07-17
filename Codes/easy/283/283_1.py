# https://quera.org/problemset/283

a = int(input())
b = int(input())

if b >= a:
    print('Wrong order!')
elif (a-b) % 2 != 0:
    print('Wrong difference!')
else:
    if a % 2 == 1:
        mid = a // 2 + 1 
        t = ((b-1) // 2)
        text = ''
        for i in range(1,a+1):
            if i in range(mid-t, mid+t+1):
                text += '* '*((a-b)//2) + '  '*b + '* '*((a-b)//2) + '\n'
            else:
                text += '* '*a +'\n'
    else:
        mid = [a // 2, a // 2+1]
        t = b // 2
        text = ''
        for i in range(1,a+1):
            if i in range(mid[0]-t+1, mid[1]+t):
                text += '* '*((a-b)//2) + '  '*b + '* '*((a-b)//2) + '\n'
            else:
                text += '* '*a +'\n'
    
    print(text)
            
            
    
    
    
    

# Code wirter Github: https://github.com/mr-mahmood