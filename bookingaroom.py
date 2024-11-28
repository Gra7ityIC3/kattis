r, n = map(int, input().split())
print(({*range(1, r + 1)} - {int(input()) for _ in range(n)} or ['too late']).pop())