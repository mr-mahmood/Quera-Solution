# https://quera.org/problemset/3404

weight = float(input())
hight = float(input())

bmi = weight / (hight*hight)
if bmi < 18.5:
    print(f'{bmi:.2f}\nUnderweight')

elif 18.5 <= bmi < 25:
    print(f'{bmi:.2f}\nNormal')

elif 25 <= bmi < 30:
    print(f'{bmi:.2f}\nOverweight')


elif bmi >= 30:
    print(f'{bmi:.2f}\nObese')





# Code wirter Github: https://github.com/mr-mahmood