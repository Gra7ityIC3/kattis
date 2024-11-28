n, x = map(int, input().split())
print('Jebb' if x >= sum(int(input()) for _ in range(n)) else 'Neibb')