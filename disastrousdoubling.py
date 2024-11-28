input()
r = 1
for b in map(int, input().split()):
    r *= 2
    if b > r:
        print('error')
        break
    r -= b
else:
    print(r % 1000000007)