n = int(input())
a = [0, *map(int, input().split())]
ans = n
for i in range(1, n + 1):
    if a[i] != -1:
        ans -= 1
        while a[i] != -1:
            a[i], i = -1, a[i]
print(ans)