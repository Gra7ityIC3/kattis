ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
while (ax - bx) * (cx - bx) + (ay - by) * (cy - by):
    ax, ay, bx, by, cx, cy = bx, by, cx, cy, ax, ay
print(ax + cx - bx, ay + cy - by)