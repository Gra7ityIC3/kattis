n = int(input())
seen, d = {}, n
for i in range(n):
    s = input()
    if s in seen:
        d = min(d, i - seen[s])
    seen[s] = i
print(max(n - d, 0))