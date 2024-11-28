n = int(input())
s = input()
g = a = 0
best, ans = -1, (0, 0)
for i in range(n - 1, - 1, -1):
    if s[i] == 'G':
        g += 1
    elif s[i] == 'A':
        a += 1
    cur = g / max(g + a, 1)
    if cur > best:
        best = cur
        ans = (g, a)
print('%d-%d' % ans)