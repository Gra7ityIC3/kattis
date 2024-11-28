from heapq import *

for _ in range(int(input())):
    input()
    heapify(pq := [*map(int, input().split())])
    ans = 0
    while len(pq) > 1:
        a, b = heappop(pq), heappop(pq)
        ans += a + b
        heappush(pq, a + b)
    print(ans)