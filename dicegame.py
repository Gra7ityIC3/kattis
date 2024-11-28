g = sum(map(int, input().split()))
e = sum(map(int, input().split()))
if g == e:
    print('Tie')
elif g > e:
    print('Gunnar')
else:
    print('Emma')