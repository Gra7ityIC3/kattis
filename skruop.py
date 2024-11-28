ans = 7
for _ in range(int(input())):
    ans = min(10, ans + 1) if input().endswith('op!') else max(0, ans - 1)
print(ans)