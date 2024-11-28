qaly = 0
for _ in range(int(input())):
    q, y = map(float, input().split())
    qaly += q * y
print(qaly)