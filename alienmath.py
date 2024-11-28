B = int(input())
D = input().split()
X = input()
ans = i = 0
for j in range(1, len(X) + 1):
    if X[i:j] in D:
        ans = ans * B + D.index(X[i:j])
        i = j
print(ans)