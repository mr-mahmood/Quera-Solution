# https://quera.org/problemset/308

def IsPalindrome(text):
    text = ''.join(filter(str.isalnum, text))
    
    reverce = text[::-1]
    if reverce.lower() == text.lower():
        print('YES')
    else:
        print('NO')
        

IsPalindrome(input())