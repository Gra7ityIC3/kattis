k = int(input())
a = input()
b = input()
print(len(a) - abs(k - sum(x == y for x, y in zip(a, b))))