n, k = map(int, input().split())
ans = cur = 0
pow10 = 1
for i in range(1, n + 1):
    if i == pow10: pow10 *= 10
    cur = (cur * pow10 + i) % k
    ans += cur == 0
print(ans)