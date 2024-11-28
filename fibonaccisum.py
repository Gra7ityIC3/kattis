n = int(input())
F = [1, 2]
while F[-1] <= n:
    F.append(F[-1] + F[-2])
ans = []
for i in range(len(F) - 2, -1, -1):
    if n >= F[i]:
        ans.append(F[i])
        n -= F[i]
print(*ans[::-1])