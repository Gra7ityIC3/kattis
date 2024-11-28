import math

for _ in range(int(input())):
    x = int(input())
    print(math.comb(2 * x, x) // (x + 1))