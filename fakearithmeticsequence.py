n = int(input())
a = [*map(int, input().split())]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        b = [a[i], a[j]]
        for k in range(j + 1, n):
            if a[k] == b[-1] + b[-2]:
                b.append(a[k])
        ans = max(ans, len(b))
print(ans)