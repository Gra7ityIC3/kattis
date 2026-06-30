n, m = map(int, input().split())
a = sorted(map(int, input().split()))

ans = a[-1]
left = 0
right = 2 * (n - m) - 1

while left < right:
    ans = max(ans, a[left] + a[right])
    left += 1
    right -= 1

print(ans)