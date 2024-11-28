import math

n = int(input())
x = [*map(int, input().split())]
num, den = 1, x[-1]
for i in range(n - 2, -1, -1):
    num += x[i] * den
    num, den = den, num
d = math.gcd(num, den)
print(f'{den // d}/{num // d}')