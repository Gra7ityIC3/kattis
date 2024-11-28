a, b = map(int, input().split())
print(~a % 2 * pow(a // 2, b, a))