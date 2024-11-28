n, k = map(int, input().split())
events = []
for _ in range(n):
    a, b = map(int,input().split())
    events.append((a, -1))
    events.append((b + k, 1))
events.sort()
count = best = 0
for _, d in events:
    count -= d
    best = max(best, count)
print(best)