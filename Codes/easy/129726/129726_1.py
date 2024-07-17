# https://quera.org/problemset/129726



def separator(ls):

    final = ([],[])

    for i in ls:

        if i%2 == 0:

            final[0].append(i)

        else:

            final[1].append(i)

    return final



print(separator([ 11, 25,89]))