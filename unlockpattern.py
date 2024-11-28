import math

a = [0] * 9
for i in range(3):
    line = [*map(int, input().split())]
    for j in range(3):
        a[line[j] - 1] = (i, j)
print(sum(math.dist(a[i], a[i + 1]) for i in range(8)))