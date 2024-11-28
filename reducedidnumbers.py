G = int(input())
SINs = [int(input()) for _ in range(G)]
m = 1
while len({s % m for s in SINs}) != G:
    m += 1
print(m)