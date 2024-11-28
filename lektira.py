n = len(s := input())
print(min(s[i::-1] + s[j:i:-1] + s[:j:-1] for i in range(n - 2) for j in range(i + 1, n - 1)))