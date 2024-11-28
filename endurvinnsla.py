input()
p = float(input())
n = int(input())
print('Jebb' if sum(input() != 'plast' for _ in range(n)) / n <= p else 'Neibb')