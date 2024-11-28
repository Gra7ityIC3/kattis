a = [0, 0, 0]
ans = 0
for c in input():
    a[int(c)] += 1
    if c < '1': ans += a[1]
    if c < '2': ans += a[2]
print(ans)