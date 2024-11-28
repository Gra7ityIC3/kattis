n = int(input())
t = sorted(map(int, input().split()))
print(max(i + t[~i] for i in range(n)) + 2)