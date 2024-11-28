def prod(x):
    y = 1
    while x:
        y *= x % 10 or 1
        x //= 10
    return y

x = int(input())
while x >= 10:
    x = prod(x)
print(x)