# https://quera.org/problemset/10325



r, c = (int(i) for i in input().split(" "))



row = 10-r+1



if c>10:

    colum = 20-c+1

    print(f"Left {row} {colum}")

else:

    colum = c

    print(f"Right {row} {colum}")

    