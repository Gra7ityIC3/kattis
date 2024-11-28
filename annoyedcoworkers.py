from heapq import *

h, c = map(int, input().split())
pq = []
for _ in range(c):
    a, d = map(int, input().split())
    pq.append((a + d, d))
heapify(pq)
for _ in range(h):
    a, d = heappop(pq)
    heappush(pq, (a + d, d))
print(max(a - d for a, d in pq))