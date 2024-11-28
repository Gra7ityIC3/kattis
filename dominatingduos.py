stack, ans = [], 0
for _ in range(int(input())):
    d = int(input())
    while stack and stack[-1] < d:
        del stack[-1]
        ans += 1
    if stack:
        ans += 1
    stack.append(d)
print(ans)