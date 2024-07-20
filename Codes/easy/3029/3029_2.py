# https://quera.org/problemset/3029

x_person, y_person = map(int, input().split())

x_friend, y_friend = map(int, input().split())


# make it more python style
print('Right') if x_person < x_friend else print('Left')

