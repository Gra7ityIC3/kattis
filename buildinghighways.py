n = int(input())
a = [*map(int, input().split())]
print(sum(a) + min(a) * (n - 2))