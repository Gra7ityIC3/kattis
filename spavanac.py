h, m = map(int, input().split())
m -= 45
print((h - (m < 0)) % 24, m % 60)