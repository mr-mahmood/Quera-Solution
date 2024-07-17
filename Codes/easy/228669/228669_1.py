# https://quera.org/problemset/228669

n = int(input())
m = int(input())
sum = 0

if n == 1:
    sum += m
elif m == 1:
    sum += n
elif n == 2 or m == 2:
    sum += n*m
else:
    sum += 2*n
    sum += 2*(m-2)
            
print(sum)

# Code wirter Github: https://github.com/mr-mahmood