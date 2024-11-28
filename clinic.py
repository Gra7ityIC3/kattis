import sys
from heapq import heappush, heappop

n, k = map(int, input().split())
pq = []
leave = set()
for line in sys.stdin:
    line = line.split()
    if line[0] == '1':
        heappush(pq, (k * int(line[1]) - int(line[3]), line[2]))
    elif line[0] == '2':
        while pq:
            m = heappop(pq)[1]
            if m not in leave:
                print(m)
                break
        else:
            print('doctor takes a break')
    else:
        leave.add(line[2])