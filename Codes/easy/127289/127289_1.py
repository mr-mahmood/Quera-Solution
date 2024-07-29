# https://quera.org/problemset/127289

text = 'codecup6'

len_text = len(text)

n = int(input())

reminder = n % len_text

print(text[reminder-1])
