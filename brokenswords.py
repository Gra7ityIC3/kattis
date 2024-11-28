TB = LR = 0
for _ in range(int(input())):
    T, B, L, R = map(int, input())
    TB += 2 - T - B
    LR += 2 - L - R
a = min(TB // 2, LR // 2)
print(a, TB - 2 * a, LR - 2 * a)