n = int(input())
ans = []
i = 1
while i * i <= n:
    if n % i == 0:
        if i != n // i:
            ans.append(n // i)
        print(i)
    i += 1
for x in reversed(ans):
    print(x)