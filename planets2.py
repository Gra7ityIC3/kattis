d, ans = {}, {}
for _ in range(int(input())):
    P, n, *s = input().split()
    for i in range(int(n)):
        d[s[i]] = P
    ans[P] = 0
for _ in range(int(input())):
    m, r = input().split()
    ans[d[r]] += int(m)
for P, m in sorted(ans.items()):
    print(P, m)