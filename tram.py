n = int(input())
a = 0
for _ in range(n):
    x, y = map(int, input().split())
    a += y - x
print(a / n)