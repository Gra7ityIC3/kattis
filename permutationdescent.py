from functools import lru_cache

@lru_cache(maxsize=None)
def PDC(n, v):
    if v == 0 or v == n - 1: return 1
    return ((v + 1) * PDC(n - 1, v) + (n - v) * PDC(n - 1, v - 1)) % 1001113

for _ in range(int(input())):
    k, n, v = map(int, input().split())
    print(k, PDC(n, v))