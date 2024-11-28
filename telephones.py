from bisect import *

while True:
    n, m = map(int, input().split())
    if n == 0: break
    start = [0] * n
    end = [0] * n
    for i in range(n):
        _, _, start[i], end[i] = map(int, input().split())
        end[i] += start[i]
    start.sort()
    end.sort()
    for _ in range(m):
        s, e = map(int, input().split())
        e += s
        print(bisect_left(start, e) - bisect_right(end, s))