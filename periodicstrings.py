n = len(s := input())
for k in range(1, n + 1):
    if n % k == 0:
        t = s[:k]
        for i in range(k, n, k):
            t = t[-1] + t[:-1]
            if s[i:i+k] != t:
                break
        else:
            print(k)
            break