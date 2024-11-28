n, e = map(int, input().split())
print(sum(str(2 ** e) in str(i) for i in range(n + 1)))