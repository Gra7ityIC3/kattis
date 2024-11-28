from math import factorial
from collections import Counter

for line in open(0):
    ans = factorial(len(line) - 1)
    for v in Counter(line).values():
        ans //= factorial(v)
    print(ans)