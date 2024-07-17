# https://quera.org/problemset/617



while True:

    n = input()

    if 1 <= int(n) <= 2_000_000_000:

        break



print("YES") if n == n[::-1] else print("NO")