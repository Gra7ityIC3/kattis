n = int(input())
h = [0] * n
s = [0] * n
for i in range(n):
    h[i], s[i] = map(int, input().split())
i, j = 0, 1
while j < n:
    while h[i] > 0:
        h[j] -= s[i]
        i, j = j, i
    i, j = j, max(j, i) + 1
print(i + 1)