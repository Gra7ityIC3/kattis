def is_weak_vertex(i):
    for j in range(n):
        if AM[i][j]:
            for k in range(j + 1, n):
                if AM[i][k] and AM[j][k]:
                    return False
    return True

while (n := int(input())) != -1:
    AM = [[*map(int, input().split())] for _ in range(n)]
    print(*(i for i in range(n) if is_weak_vertex(i)))