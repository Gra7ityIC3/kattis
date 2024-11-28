ans = 0
for _ in range(int(input())):
    color = input().lower()
    ans += 'pink' in color or 'rose' in color
print(ans or 'I must watch Star Wars with my daughter')