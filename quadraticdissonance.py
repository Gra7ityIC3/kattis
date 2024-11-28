A, B, C, D = map(int, input().split())
h = lambda x: max(x * x + A * x + B, x * x + C * x + D)
x = min(-A / 2, -C / 2, A == C or (D - B) / (A - C), key=h)
print(x, h(x))