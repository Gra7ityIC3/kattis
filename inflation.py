n = int(input())
c = sorted(map(int, input().split()))
ans = 1
for i in range(n):
    if c[i] / (i + 1) > 1:
        ans = 'impossible'
        break
    ans = min(ans, c[i] / (i + 1))
print(ans)