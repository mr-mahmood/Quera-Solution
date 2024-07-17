# https://quera.org/problemset/282

while True:
    n = int(input())
    if 2<=n<=200000:
        break
sum = 0 
for i in range(1, n):
    if n%i == 0:
        sum += i
if sum > n or sum < n:
    print("NO")
elif sum == n:
    print("YES")

# Code wirter mr-mahmood
# Github: https://github.com/mr-mahmood