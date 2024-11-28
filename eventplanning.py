n, b, h, w = map(int, input().split())
ans = b + 1
for _ in range(h):
    p = int(input())
    for a in map(int, input().split()):
        if a >= n and n * p < ans:
            ans = n * p
print(ans if ans <= b else 'stay home')