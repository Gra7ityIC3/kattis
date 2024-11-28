r, c = map(int, input().split())
grid = [input() for _ in range(r)]
grid += map(''.join, zip(*grid))
print(min(word for line in grid for word in line.split('#') if len(word) >= 2))