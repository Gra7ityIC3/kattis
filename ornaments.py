from math import *

while True:
    r, h, s = map(int, input().split())
    if r == 0: break
    l = 2 * sqrt(h * h - r * r)
    l += (2 * pi - 2 * acos(r / h)) * r
    l *= 1 + s / 100
    print(f'{l:.2f}')