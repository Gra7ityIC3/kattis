ans = 0
for _ in range(int(input())):
    i, word = input().split()
    if word == 'nej':
        ans = max(ans, int(i))
print(ans)