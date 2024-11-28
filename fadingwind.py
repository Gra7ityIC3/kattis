h, k, v, s = map(int, input().split())
d = 0
while h:
    v += s
    v -= max(1, v // 10)
    h += v >= k
    h -= 0 < v < k
    v *= h > 0
    h *= v > 0
    d += v
    s -= s > 0
print(d)