n, k = map(int, input().split())
x = [*map(int, input().split())]
print(*x[k-1::k])