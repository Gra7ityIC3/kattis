ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
y = 1
while (ds + y) % ys or (dm + y) % ym:
    y += 1
print(y)