# https://quera.org/problemset/176776

fans = input()

paozo_fans = fans.split('1')

length = [len(i) for i in paozo_fans]

print(max(length))
