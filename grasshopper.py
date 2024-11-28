from collections import deque

dr = (-2, -1, 1, 2, 2, 1, -1, -2)
dc = (1, 2, 2, 1, -1, -2, -2, -1)

for line in open(0):
    r, c, gr, gc, lr, lc = map(int, line.split())
    dist = [[-1] * (c + 1) for _ in range(r + 1)]
    dist[gr][gc] = 0
    q = deque([(gr, gc)])
    while q and dist[lr][lc] == -1:
        gr, gc = q.popleft()
        for d in range(8):
            nr = gr + dr[d]
            nc = gc + dc[d]
            if 1 <= nr <= r and 1 <= nc <= c and dist[nr][nc] == -1:
                dist[nr][nc] = dist[gr][gc] + 1
                q.append((nr, nc))
    print(dist[lr][lc] if q else 'impossible')