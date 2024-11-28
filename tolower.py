p, t = map(int, input().split())
print(sum(all([input()[1:].islower() for _ in range(t)]) for _ in range(p)))