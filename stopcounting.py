n = int(input())
a = [*map(int, input().split())]
ans = prefix = suffix = 0
for i in range(n):
    prefix += a[i]
    suffix += a[~i]
    ans = max(ans, prefix / (i + 1), suffix / (i + 1))
print(ans)