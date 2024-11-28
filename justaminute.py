a = b = 0
for _ in range(int(input())):
    m, s = map(int, input().split())
    a += m
    b += s
print(b / 60 / a if b / a > 60 else 'measurement error')