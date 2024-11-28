cost = {'.': 20, 'O': 10, '\\': 25, '/': 25, 'A': 35, '^': 5, 'v': 22}
n, m = map(int, input().split())
print(sum(cost[c] for _ in range(n) for c in input()))