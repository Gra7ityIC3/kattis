n, d, k = map(int, input().split())
print(sum(int(input()) + 14 <= d + k for _ in range(n)))