# https://quera.org/problemset/60134

def fruits(fruit_list):
    final = {}
    for i in fruit_list:
        f1, f2, f3 = False, False, False
        name= ''
        for j,k in i.items():
            if j == 'name':
                name = k
            elif j == 'shape':
                if k == 'sphere':
                    f1 = True
            elif j == 'mass':
                if 300 <= k <= 600:
                    f2 = True
            elif j == 'volume':
                if 100 <= k <= 500:
                    f3 = True
        if f1 and f2 and f3:
            if name not in final.keys():
                final[name] = 1
            else:
                final[name] += 1
    return final

    