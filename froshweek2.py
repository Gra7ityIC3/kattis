n, m = map(int, input().split())
t = sorted(map(int, input().split()), reverse=True)
l = sorted(map(int, input().split()), reverse=True)
i = j = ans = 0
while i < n and j < m:
    if t[i] <= l[j]:
        ans += 1
        j += 1
    i += 1
print(ans)