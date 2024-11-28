MOD = 10 ** 9 + 7
n = int(input())
s = input()
n1 = n12 = ans = 0
for i in range(0, 2 * n, 2):
    if s[i] == '1':
        n1 += 1
    elif s[i] == '2':
        n12 = (2 * n12 + n1) % MOD
    else:
        ans += n12
print(ans % MOD)