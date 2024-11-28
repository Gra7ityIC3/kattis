_, *a = map(int, open(0))
l, r = 0, sum(a)
ans = 0
for x in a:
    l += x * x
    r -= x
    ans = max(ans, l * r)
print(ans)