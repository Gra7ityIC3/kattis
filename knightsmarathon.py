nx, ny = map(int, input().split())
kx, ky = map(int, input().split())
cx, cy = map(int, input().split())
x, y = abs(cx - kx), abs(cy - ky)
if x < y:
    x, y = y, x
if x == 1 and y == 0:
    print(3)
elif x == 2 and y == 2:
    print(4)
elif x == 1 and y == 1 and ((cx == 0 or cx == nx - 1) and (cy == 0 or cy == ny - 1) or
                            (kx == 0 or kx == nx - 1) and (ky == 0 or ky == ny - 1)):
    print(4)
else:
    delta = x - y
    print(delta - 2 * ((delta - y) // (3 if y > delta else 4)))