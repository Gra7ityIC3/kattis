a = b = c = -1
for _ in range(int(input())):
    t, d = map(int, input().split())
    a = max(a, (d - b) // (t - c))
    b, c = d, t
print(a)