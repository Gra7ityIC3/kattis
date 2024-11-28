import heapq
import sys
from collections import deque

while n := sys.stdin.readline():
    stack, q, pq = [], deque(), []
    is_stack = is_q = is_pq = True
    for _ in range(int(n)):
        op, x = map(int, sys.stdin.readline().split())
        if op == 1:
            stack.append(x)
            q.append(x)
            heapq.heappush(pq, -x)
        else:
            is_stack = is_stack and len(stack) and stack.pop() == x
            is_q = is_q and len(q) and q.popleft() == x
            is_pq = is_pq and len(pq) and -heapq.heappop(pq) == x
    if is_stack + is_q + is_pq > 1:
        print('not sure')
    elif is_stack:
        print('stack')
    elif is_q:
        print('queue')
    elif is_pq:
        print('priority queue')
    else:
        print('impossible')