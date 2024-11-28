k, a, b = map(int, open(0))
ans = []
for x in range(k // a + 1):
    if (k - a * x) % b == 0:
        ans.append((x, (k - a * x) // b))
print(len(ans))
for x, y in ans:
    print(x, y)