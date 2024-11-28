n, *d = map(int, open(0))
ans = []
for k in range(2, n + 1):
    if n % k == 0:
        i = n // k
        for j in range(i, n, i):
            if max(d[j-i:j]) >= min(d[j:j+i]):
                break
        else:
            ans.append(k)
if ans:
    print(*ans, sep='\n')
else:
    print(-1)