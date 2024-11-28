n, c = map(int, input().split())
ans = [0] * n
max_pos = max_neg = -1000000
for i, x in enumerate(map(int, input().split())):
    max_pos = max(max_pos, x + c * i)
    max_neg = max(max_neg, -x + c * i)
    ans[i] = max(x - c * i + max_neg, -x - c * i + max_pos)
print(*ans)