input()
a = [*map(int,input().split())]
print(max(2 * max(a), sum(a)))