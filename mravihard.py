from math import log10

def dfs(L, u):
    for v, x, t in AL[u]:
        l = L + log10(x) - 2
        if l > 0 and t: l *= 2
        if not dfs(l, v): return False
    return k[u] == -1 or L >= log10(k[u])

n = int(input())
AL = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, x, t = map(int, input().split())
    AL[a].append((b, x, t))
k = [0, *map(float, input().split())]
lo, hi = 0, 2e9
while hi - lo > 0.001:
    mid = (lo + hi) / 2
    if dfs(log10(mid), 1): 
        hi = mid
    else:
        lo = mid
print(hi)