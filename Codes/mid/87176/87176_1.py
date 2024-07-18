# https://quera.org/problemset/87176

def game(number):
    
    number = str(number)
    
    a = int(number[0])
    b = int(number[1])
    
    if b >= a:
        
        return b - a
    
    else:
        
        return a - b
    
    