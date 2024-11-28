n, k = map(int, input().split())
ans = last = 0
for _ in range(k):
    h = int(input())
    ans += (h - last) * (n - h + 1)
    last = h
print(ans)