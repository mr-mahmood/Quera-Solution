# https://quera.org/problemset/108665
while True:

    name = input()

    if len(name) <= 6:

        name = name.lower()

        break

key = ['a', 'e', 'i', 'o', 'u']

key_sum = 0

for i in name:

    if i in key:

        key_sum += 1

print(pow(2,key_sum))