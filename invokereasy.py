a, b = map(int, input().split())
c, d = map(int, input().split())
e = c * c + d * d
print((a * c + b * d) / e, (b * c - a * d) / e)