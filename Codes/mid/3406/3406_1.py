# https://quera.org/problemset/3406

num_1 = input()
num_2 = input()

if int(num_1[::-1]) > int(num_2[::-1]):
    print(f'{num_2} < {num_1}')
    
elif int(num_2[::-1]) > int(num_1[::-1]):
    print(f'{num_1} < {num_2}')
    
elif int(num_1[::-1]) == int(num_2[::-1]):
    print(f'{num_2} = {num_1}')
   
# Code wirter Github: https://github.com/mr-mahmood