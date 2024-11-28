from bisect import bisect_left

n, m = map(int, input().split())
a = sorted(int(input()) for _ in range(n))
print(sum(a[bisect_left(a, x := int(input()))] - x for _ in range(m)))