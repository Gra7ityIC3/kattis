from math import gcd

c, d = map(int, input().split())
a = b = 0
for i, s in enumerate(input().split(), c):
    if 'F' in s: a = gcd(a, i)
    if 'B' in s: b = gcd(b, i)
print(a or d + 1, b or d + 1)