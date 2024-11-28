m = int(input())
n = int(input())
print(sum(input().count('.') for _ in range(n)) / (m * n))