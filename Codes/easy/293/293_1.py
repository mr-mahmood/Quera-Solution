# https://quera.org/problemset/293

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

a = int(input())
b = int(input())

for i in range(a, b+1):
    if is_prime(i):
        print(i)

# Code wirter Github: https://github.com/mr-mahmood