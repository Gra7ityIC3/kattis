t, k = map(int, input().split())
ans = 0
for i in range(2, t + 1):
    ans = (ans + k) % i
print(ans)