from itertools import accumulate

n = int(input())
s = [0] * n
a = [0] * n
for i in range(n):
    s[i], a[i] = map(int, input().split())
s.sort()
a.sort()
print(sum(accumulate(i * (s[i] - s[i - 1] + a[i] - a[i - 1]) for i in range(1, n))))