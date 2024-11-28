D, R, T = map(int, open(0))
n = int((2 * D - 2 + (-4 * D * D + 16 * (R + T) + 148) ** 0.5) / 4)
print(R - (n - 3) * (4 + n) // 2)