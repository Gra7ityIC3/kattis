import math

for _ in range(int(input())):
    r, n = map(int, input().split())
    ans = area = math.pi * r * r
    for _ in range(n - 1):
        ans += area
        area *= 0.75
    print(ans)