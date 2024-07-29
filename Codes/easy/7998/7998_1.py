# https://quera.org/problemset/7998

n = int(input())

name = ''
cap = 'lower' # at start
for i in range(n):
    keyboard_input = input()
    
    if keyboard_input == 'CAPS':
        
        if cap == 'lower':
            cap = 'upper'
        
        else:
            cap = 'lower'
    
    else:
        
        if cap == 'lower':
            name += keyboard_input.lower()
            
        else:
            name += keyboard_input.upper()
            
print(name)