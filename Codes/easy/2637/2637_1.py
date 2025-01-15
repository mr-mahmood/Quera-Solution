# https://quera.org/problemset/2637

n = int(input())
max = 0
for i in range(1, n):
    row_line = i
    coloum_line = n - i
    if (row_line+1) * (coloum_line+1) > max:
        max = (row_line+1) * (coloum_line+1)
        """
        (row_line+1) * (coloum_line+1) because every single line that you draw make numbner_of_line + 1 land
        for example 2 vertical line make 3 land and 4 make 5 now if we draw a horizental line on this 5 land it became 10 land
        which is (4+1) * (1+1) = 10
        """
        
print(max)

# Code wirter Github: https://github.com/mr-mahmood