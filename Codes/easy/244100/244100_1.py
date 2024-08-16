# https://quera.org/problemset/244100

text = input()

#split it from where .NET is located
text = text.split('.NET')

# join split text with Golang
text = 'Golang'.join(text)

print(text)