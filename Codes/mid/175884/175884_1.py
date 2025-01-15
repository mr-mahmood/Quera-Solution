# https://quera.org/problemset/175884

def calculate_floor(string):
    floor = 0
    for i in string:
        if i == 'U':
            floor += 1
        else:
            floor -= 1
            
    return floor

# Code wirter Github: https://github.com/mr-mahmood