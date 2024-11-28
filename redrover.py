n = len(s := input())
ans = n
for i in range(n):
    for j in range(i + 1, n + 1):
        ans = min(ans, len(s.replace(t := s[i:j], 'M')) + len(t))
print(ans)