x = int(input())
i, k = 2, 0
while i * i <= x:
    if x % i:
        i += 1
    else:
        x //= i
        k += 1
print(k + (x > 1))