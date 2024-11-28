input()
print(min(map(sum, enumerate(reversed(sorted([*map(int, input().split()), 0]))))))