n = int(input())
F = []
a = b = 1
while b <= n:
    F.append(b)
    a, b = b, a + b
for i in range(len(F)):
    if n >= F[~i]:
        n -= (ans := F[~i])
print(ans)