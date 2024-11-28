MOD = 1000000007
inversions = ones = 0
branches = 1
for c in input():
    if c == '0':
        inversions = (inversions + ones) % MOD
    elif c == '1':
        ones += branches
    else:
        inversions = (2 * inversions + ones) % MOD
        ones = (2 * ones + branches) % MOD
        branches = 2 * branches % MOD
print(inversions)