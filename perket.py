def solve(i, x, y):
    if i == n:
        return abs(x - y) if y else 10 ** 9
    return min(solve(i + 1, x, y), solve(i + 1, x * s[i], y + b[i]))

n = int(input())
s, b = [0] * n, [0] * n
for i in range(n):
    s[i], b[i] = map(int, input().split())
print(solve(0, 1, 0))