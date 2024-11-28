from math import *

for line in open(0):
    n = int(line)
    print(1 + int(n and 0.5 * log10(2 * pi * n) + n * log10(n / e)))