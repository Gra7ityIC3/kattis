from bisect import bisect_right

primes = [0]
bs = [True] * 20001
for i in range(2, 20001):
    if bs[i]:
        for j in range(i * i, 20001, i):
            bs[j] = False
        primes.append(i)

for _ in range(int(input())):
    n, d = map(int, input().split())
    x1 = y1 = ans = 0
    for _ in range(n):
        x2, y2 = map(int, input().split())
        d -= ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        ans += d >= 0
        x1, y1 = x2, y2
    print(primes[bisect_right(primes, ans) - 1])