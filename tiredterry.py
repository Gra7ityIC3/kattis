n, p, d = map(int, input().split())
s = input() * 2
sleep = sum(s[i] == 'Z' for i in range(p))
ans = 0
for i in range(n):
    ans += sleep < d
    sleep += s[i + p] == 'Z'
    sleep -= s[i] == 'Z'
print(ans)