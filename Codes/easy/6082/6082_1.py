# https://quera.org/problemset/6082

n, m = map(int, input().split(' '))

stars = 0
for i in range(n):
    text = input()
    stars += text.count('*')
    
print(stars)

# Code wirter Github: https://github.com/mr-mahmood