# https://quera.org/problemset/9722

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def check(n):
    if n == 1:
        return ['2', '3', '5', '7']
    else:
        num = check(n-1)
        final = []       
        for i in num:
            for j in range(10):
                if is_prime(int(i+str(j))):
                    final.append(i+str(j))
        return final
    
while True:
    n = int(input())
    if 1 <= n <= 8 :
        break  

final = check(n)            
print(*final, sep='\n')