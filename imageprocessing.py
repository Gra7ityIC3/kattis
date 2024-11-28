h, w, n, m = map(int, input().split())
img = [[*map(int, input().split())] for _ in range(h)]
kernel = [[*map(int, input().split())] for _ in range(n)]
for i in range(h - n + 1):
    print(*(sum(kernel[~k][~l] * img[i + k][j + l] for k in range(n) for l in range(m)) for j in range(w - m + 1)))