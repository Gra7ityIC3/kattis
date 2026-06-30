n, x, m = map(int, input().split())
crates = [0] * (n + 1)
for _ in range(m):
    crates[int(input())] += 1
print(min(sum(crates[1:x]), sum(crates[n:x-1:-1])))