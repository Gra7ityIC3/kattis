ans = right = 0
for c in input():
    if c == '>':
        right += 1
    elif c == '<':
        ans += right
print(ans)