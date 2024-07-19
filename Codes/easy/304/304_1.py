# https://quera.org/problemset/304

def base_to_exp(base, exp, result):
    if exp == 0:
        return result
    result = base * result 
    exp -= 1
    return base_to_exp(base, exp, result)

base = float(input())
exp = int(input())

print(f'{base_to_exp(base, exp, 1.0):0.3f}')
