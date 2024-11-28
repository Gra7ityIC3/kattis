input()
ans, req = 0, 1
side = 2 ** -0.75
for x in map(int, input().split()):
    ans += req * side
    req = req * 2 - x
    side /= 2 ** 0.5
print(ans if req <= 0 else 'impossible')