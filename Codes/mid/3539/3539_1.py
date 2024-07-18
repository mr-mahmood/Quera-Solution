# https://quera.org/problemset/3539

def count(n):
    result = 0
    count = 0
    for i in n:
        if len(n) == 1:
            return n, 0
        result += int(i) 
        count += 1
    return result, count

while True:
    n = input()
    if 0 <= int(n) <= 1_000_000_000_000_000_000:
        break

a,b = count(n)
while b != 0:
    a,b = count(str(a))
    
        
print(a)