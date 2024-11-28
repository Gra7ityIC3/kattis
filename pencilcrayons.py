n, k = map(int, input().split())
print(sum(k - len({*input().split()}) for _ in range(n)))