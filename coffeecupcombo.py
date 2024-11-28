n = int(input())
s = input()
print(sum('1' in s[max(0, i - 3):i] for i in range(1, n + 1)))