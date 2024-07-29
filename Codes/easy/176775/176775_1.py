# https://quera.org/problemset/176775

import math

def is_power_of_two(x):
    return (x & (x - 1)) == 0 and x != 0

def is_pseudo_binary(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return is_power_of_two(divisors_sum)


n = int(input())


if is_pseudo_binary(n):
    print(1)
else:
    print(0)
