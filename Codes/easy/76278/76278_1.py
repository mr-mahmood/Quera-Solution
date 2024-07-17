# https://quera.org/problemset/76278



def calculator(n, m, li):

    i = 0

    final = []

    while i < n:

        temp = []

        j = 0

        if i+m < n:

            temp = li[i:i+m:]

            i = i+m

        else:

            temp = li[i::]

        for i in temp:

            j += i

        final.append(j)

    result = 0

    for i in range(len(final)):

        if i%2 == 0:

            result += final[i]

        else:

            result -= final[i]

    return result            