def binary_search(x):
    lo, hi = 0, len(ans)
    while lo < hi:
        mid = (lo + hi) // 2
        if ans[mid][-1] < x:
            hi = mid
        else:
            lo = mid + 1
    return lo

input()
ans = []
for x in map(int, input().split()):
    pos = binary_search(x)
    if pos == len(ans):
        ans.append([x])
    else:
        ans[pos].append(x)

print(len(ans))
for a in ans: print(*a)