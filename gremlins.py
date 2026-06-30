n, m = map(int, input().split())
items = [input() for _ in range(n)]
d = {input(): i for i in range(1, m + 1)}
for item in items:
    print(d.get(item, 'stolen!'))