k, q = map(int, input().split())
solved = [0] * k
for _ in range(q):
    a, b = map(int, input().split())
    solved[b - 1] += 1
print(min(solved))