l, r = map(int, input().split())
print((r - l + 1) * (l + r) * 5 % 9)