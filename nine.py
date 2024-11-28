MOD = 1000000007
for _ in range(int(input())):
    print(8 * pow(9, int(input()) - 1, MOD) % MOD)