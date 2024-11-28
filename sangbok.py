t = int(input().split()[0]) * 60
ans = 0
for s in sorted(map(int, input().split())):
    if ans + s > t:
        break
    ans += s
print(ans)