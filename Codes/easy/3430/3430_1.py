# https://quera.org/problemset/3430
text = input()
print(text)
for i in range(1, len(text)):
    print(f'{text[i]*(i+1)}{text[i+1::]}')

# Code wirter Github: https://github.com/mr-mahmood