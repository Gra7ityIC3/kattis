n, m = map(int, input().split())
a = [1] * m
for _ in range(n):
    for i, c in enumerate(input()):
        a[i] &= c == '_'
print(sum(a, 1))