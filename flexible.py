W, P = map(int, input().split())
L = [0, *map(int, input().split()), W]
ans = set()
for i in range(P + 1):
    for j in range(i + 1, P + 2):
        ans.add(L[j] - L[i])
print(*sorted(ans))