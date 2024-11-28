bal = ans = 0
for _ in range(int(input())):
    bal += int(input())
    ans = min(ans, bal)
print(-ans)