n = int(input())
k = [0, *map(int, input().split())]
ans = 0
for i in range(1, n + 1):
    if k[i] == i or k[i] == -1:
        continue
    while k[i] != -1:
        k[i], i = -1, k[i]
        ans += 1
    ans += 1
print(ans)