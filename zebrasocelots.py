n = int(input())
print(sum(1 << n - i - 1 for i in range(n) if input() == 'O'))