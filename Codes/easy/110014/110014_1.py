# https://quera.org/problemset/110014

airpod1 = input().split(" ")
airpod2 = input().split(" ")


if airpod1[0] == airpod2[1] or airpod1[1] == airpod2[0] or airpod1[0] == airpod1[1] or airpod2[0] == airpod2[1]:
    print('YES')
    
else:
    print('NO')
    
# Code wirter Github: https://github.com/mr-mahmood