# https://quera.org/problemset/2530

wrong_speels = {
    't':['t', 'k'],
    'd':['d', 'g'],
    'l':['l', 'r'],
    'f':['f', 'r'],
}

word = input().lower()

all_possibles_words = 1
for i in word:
    if i in wrong_speels.keys():
        all_possibles_words *= len(wrong_speels[i])
        
print(all_possibles_words)
 
# Code wirter Github: https://github.com/mr-mahmood