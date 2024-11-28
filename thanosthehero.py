n = int(input())
a = [*map(int, input().split())]
ans = 0
for i in range(n - 2, -1, -1):
    if a[i] >= a[i + 1]:
        if a[i + 1] == 0:
            print(1)
            break
        ans += a[i] - a[i + 1] + 1
        a[i] = a[i + 1] - 1
else:
    print(ans)