n = int(input())
t = sorted(map(int, input().split()))
a = [0] * n
a[::2], a[1::2] = t[n//2:], t[n//2-1::-1]
print(*a)