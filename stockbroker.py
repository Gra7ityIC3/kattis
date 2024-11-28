ans, prev = 100, 500
for _ in range(int(input())):
    curr = int(input())
    if curr > prev:
        ans += min(ans // prev, 100000) * (curr - prev)
    prev = curr
print(ans)