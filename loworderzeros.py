digits = (1, 1, 2, 6, 4, 2, 2, 4, 2, 8)
pow2 = (6, 2, 4, 8)

def L(n):
    if n < 10:
        return digits[n]
    a, b = n // 5, n % 5
    return (pow2[a % 4] * L(a) * L(b)) % 10

while i := int(input()):
    print(L(i))