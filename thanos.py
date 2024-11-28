from math import log2

for _ in range(int(input())):
    p, r, f = map(int, input().split())
    print(int(log2(f / p) / log2(r)) + 1 if p <= f else 0)