from math import log2

while y := int(input()):
    f, w, n = 0, 2 ** (y // 10 - 194), 1
    while f < w:
        n += 1
        f += log2(n)
    print(n - 1)