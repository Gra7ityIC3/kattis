n, h, c = map(int, input().split())
effort = [sorted(map(int, input().split())) for _ in range(n)]
ans = 0
for j in range(h):
    effort.sort(key=lambda x: x[j])
    for i in range(n):
        c -= effort[i][j]
        if c < 0:
            print(ans)
            exit()
        ans += 1
print(ans)