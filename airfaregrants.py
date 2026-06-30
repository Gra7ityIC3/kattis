a = [int(input()) for _ in range(int(input()))]
min_val, max_val = min(a), max(a)
print(max(min_val - max_val // 2, 0))