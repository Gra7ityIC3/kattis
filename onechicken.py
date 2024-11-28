n, m = map(int, input().split())
if n < m:
    print(f"Dr. Chaz will have {m - n} piece{'s' * (m - n > 1)} of chicken left over!")
else:
    print(f"Dr. Chaz needs {n - m} more piece{'s' * (n - m > 1)} of chicken!")