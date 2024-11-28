n = int(input())
k = [*map(int, input().split())]
a = [*map(int, input().split())]
b = [*map(int, input().split())]
print(*(sorted((k[i], a[i], b[i]))[1] for i in range(n)))