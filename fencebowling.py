from math import *
k, w, l = map(int, input().split())
print(atan2(l / (2 ** k - 1) / 3, w / 2) * 180 / pi)