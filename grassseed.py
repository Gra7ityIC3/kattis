c = float(input())
s = 0
for _ in range(int(input())):
    w, l = map(float, input().split())
    s += w * l
print(s * c)