ans = 0
for r1 in range(4):
    for c1, c in enumerate(input()):
        if c != '.':
            r2, c2 = divmod(ord(c) - 65, 4)
            ans += abs(r1 - r2) + abs(c1 - c2)
print(ans)