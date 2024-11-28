for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [[*map(int, input().split())] for _ in range(n)]
    b = [0, *map(int, input().split())]
    print(sum(min(b[a[i][j]] for j in range(1, len(a[i]) - 1)) * a[i][-1] for i in range(n)))