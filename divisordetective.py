n = int(input())

ans = 0
i = 1

while i <= n:
    q = n // i
    last = n // q

    ans += q * (last - i + 1)
    i = last + 1

print(ans)