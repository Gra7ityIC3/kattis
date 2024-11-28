R, B = map(int, input().split())
L = int(R + 4 + ((R + 4) ** 2 - 16 * (R + B)) ** 0.5) // 4
W = (R + B) // L
print(max(L, W), min(L, W))