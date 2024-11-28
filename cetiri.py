a, b, c = sorted(map(int, input().split()))
print(4 * a + 6 * min(b - a, c - b) - a - b - c)