import math

while True:
    r, m, c = map(float, input().split())
    if r == 0: break
    print(math.pi * r * r, c / m * 4 * r * r)