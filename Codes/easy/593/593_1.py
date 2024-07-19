# https://quera.org/problemset/593
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
        
def check(number, after):
    
    count = 0
    i = 1
    while True:
        if is_prime(number+i):
            count += 1
            if count == after:
                return int(number+i)
        
        i += 1
    
if __name__ == '__main__':
    number = input()
    sum_num = sum([int(i) for i in list(number)]) 

    print(check(int(number), sum_num))