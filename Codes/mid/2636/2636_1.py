# https://quera.org/problemset/2636

values = [1, 1, 2, 2, 2, 8]

inputs = list(map(int, input().split(' ')))

change = [values[i]-inputs[i] for i in range(6)]

print(*change, sep=' ')

# Code wirter Github: https://github.com/mr-mahmood