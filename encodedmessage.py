for _ in range(int(input())):
    n = int(len(s := input()) ** 0.5)
    print(''.join(s[n-i-1::n] for i in range(n)))