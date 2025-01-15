# https://quera.org/problemset/176774

fingers = int(input())
hands = int(input())
num1 = int(input())
num2 = int(input())

if (num1+num2) % (hands*fingers) != 0:
    print((num1+num2) % (hands*fingers))  

elif (num1+num2) % (hands*fingers) == 0 and num1 != 0 and num2 != 0:
    print(hands*fingers)

elif (num1+num2) % (hands*fingers) == 0 and num1 == 0 and num2 == 0:
    print(0)
    
'''
so it send reminder for sum of numbers base on fingers in hands which is total fingers
if if became 0 it mean monster open all his fingers so we hav to add an if esttatment
if num1 and num2 arent 0 then if value of remind is 0 the monster open all his fingers so we print hands*fingers
otherwise we print (num1+num2) % (hands*fingers)
'''

# Code wirter Github: https://github.com/mr-mahmood