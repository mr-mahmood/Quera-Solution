# https://quera.org/problemset/148099
import numpy

while True:

    n = int(input())

    if 1 <= n <= 100:

        break

while True:

    main_list = [int(i) for i in input().split(' ')]

    if 1 <= len(main_list) <= 100:

        break

final_list = []

for i in main_list:

    if int(i) not in final_list:

        final_list.append(int(i))

    else:

        final_list.remove(int(i))

if len(final_list) > 0:

    res = numpy.bitwise_xor.reduce(final_list)

    print(res)

else:

    print(0)



    