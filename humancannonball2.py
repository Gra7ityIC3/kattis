from math import *

for _ in range(int(input())):
    v0, theta, x1, h1, h2 = map(float, input().split())
    theta = radians(theta)
    t = x1 / v0 / cos(theta)
    y = v0 * t * sin(theta) - 9.81 * t * t / 2
    print('Safe' if h1 + 1 <= y <= h2 - 1 else 'Not Safe')