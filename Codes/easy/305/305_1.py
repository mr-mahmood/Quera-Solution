# https://quera.org/problemset/305
def gcd(a, b):
    
    # Everything divides 0 
    if (b == 0):
         return a
    return gcd(b, a%b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(gcd(a, b))