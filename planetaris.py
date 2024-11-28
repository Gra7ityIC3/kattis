n, a = map(int, input().split())
ans = 0
for e in sorted(map(int, input().split())):
    if a <= e: break
    a -= e + 1
    ans += 1
print(ans)