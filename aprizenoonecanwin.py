_, X = map(int, input().split())
leqX = mleq = 0
mgt = X + 1
for x in map(int, input().split()):
    if x <= X // 2:
        leqX += 1
        mleq = max(mleq, x)
    else:
        mgt = min(mgt, x)
print(leqX + (mleq + mgt <= X) or 1)