from functools import lru_cache

@lru_cache(maxsize=None)
def f(x, y):
    if x <= 0 or y <= 0: return d
    return sum(f(x - ab[i], y - ab[i + 1]) for i in range(0, len(ab), 2)) + c

for _ in range(int(input())):
    *ab, c, d = map(int, input().split())
    xy = [*map(int, input().split())]
    for i in range(0, len(xy), 2):
        print(f(xy[i], xy[i + 1]))
    print()
    f.cache_clear()