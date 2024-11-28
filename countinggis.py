MOD = 10 ** 9 + 7
n, l = map(int, input().split())
g = [0, *map(int, input().split())]
if any(g[i] <= g[i - 1] for i in range(2, l + 1)) or g[l] != n:
    print(0)
else:
    spots, ans = 0, 1
    for i in range(l, 0, -1):
        spots += 1
        for _ in range(g[i] - g[i - 1] - 1):
            ans = (ans * spots) % MOD
            spots += 1
    print(ans)