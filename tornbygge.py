n = int(input())
x = [*map(int, input().split())]
print(sum(x[i] > x[i - 1] for i in range(1, n)) + 1)