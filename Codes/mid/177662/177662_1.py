# https://quera.org/problemset/177662

def can_distribute_chocolates(n, m, chocolates):

    remainders = {-1}
    
    for chocolate in chocolates:
        new_remainders = set() # set variable dont allow repeted values to be store
        for remainder in remainders:
            
            if remainder == -1 : 
                remainder = 0
                
            new_remainders.add((remainder + chocolate) % m)
        
        remainders.update(new_remainders)
        
        if 0 in new_remainders:
            return True
    
    return 0 in remainders


n, m = map(int, input().split())
chocolates = list(map(int, input().split()))


if can_distribute_chocolates(n, m, chocolates):
    print("YES")
else:
    print("NO")