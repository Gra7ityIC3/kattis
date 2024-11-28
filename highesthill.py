n = int(input())
h = [*map(int, input().split())]
ans = 0
for i in range(1, n - 1):
    if h[i - 1] < h[i] >= h[i + 1]:
        l = r = i
        while l and h[l - 1] <= h[l]: l -= 1
        while r + 1 < n and h[r] >= h[r + 1]: r += 1
        ans = max(ans, min(h[i] - h[l], h[i] - h[r]))
print(ans)