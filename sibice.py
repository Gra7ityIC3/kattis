n, w, h = map(int, input().split())
for _ in range(n):
    print('DA' if w * w + h * h >= int(input()) ** 2 else 'NE')