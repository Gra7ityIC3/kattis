r, c = map(int, input().split())
s = int(input())
a = [[*map(int, input().split())] for _ in range(r)]
ans = 0
for i in range(1, r - 1):
    for j in range(1, c - 1):
        diagonal_sum = a[i - 1][j - 1] + a[i - 1][j + 1] + a[i + 1][j - 1] + a[i + 1][j + 1]
        if a[i][j] == s and diagonal_sum % s == 0:
            ans += 1
print(ans)