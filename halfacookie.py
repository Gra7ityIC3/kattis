from math import *

for line in open(0):
    r, x, y = map(float, line.split())
    if x * x + y * y > r * r:
        print('miss')
    else:
        d = (x * x + y * y) ** 0.5
        theta = 2 * acos(d / r)
        a = r * r / 2 * (theta - sin(theta))
        print(pi * r * r - a, a)