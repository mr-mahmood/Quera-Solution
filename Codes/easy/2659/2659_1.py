# https://quera.org/problemset/2659

misstakes = 0
n = int(input())
testcase = input()
write = input()

for i in range(n):
    if write[i] != testcase[i]:
        misstakes += 1
        
print(misstakes)

# Code wirter Github: https://github.com/mr-mahmood