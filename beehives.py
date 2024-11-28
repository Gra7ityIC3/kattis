from math import dist

while True:
    d, n = map(eval, input().split())
    if n == 0: break
    hives = [[*map(float, input().split())] for _ in range(n)]
    sour = sweet = 0
    for hive1 in hives:
        if any(dist(hive1, hive2) <= d for hive2 in hives if hive1 != hive2):
            sour += 1
        else:
            sweet += 1
    print(f'{sour} sour, {sweet} sweet')