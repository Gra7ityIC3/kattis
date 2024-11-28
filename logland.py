MOD = 10 ** 9 + 7

input()
leave = extras = 0
cur = 1
for has in map(int, input().split()):
    has += extras
    if has & 1 and extras == 0:
        leave = (leave + cur) % MOD
    extras = has // 2
    cur = (cur * 2) % MOD
print(leave)