k, r = map(int, input().split())
ing = [*map(int, input().split())]
ans = 0
for _ in range(r):
    *amt, price = map(int, input().split())
    ans = max(ans, min(ing[i] // amt[i] for i in range(k) if amt[i]) * price)
print(ans)