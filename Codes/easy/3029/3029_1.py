# https://quera.org/problemset/3029

x_person, y_person = map(int, input().split())

x_friend, y_friend = map(int, input().split())

if x_friend > x_person:
    print('Right')
    
else:
    print('Left')
