ans = 0
prev = ''
for _ in range(int(input())):
    curr = input()
    if curr == 'sober' and prev == 'drunk':
        ans += 1
    prev = curr
print(ans)