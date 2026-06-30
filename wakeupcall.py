n, m = map(int, input().split())
sum1 = sum(map(int, input().split()))
sum2 = sum(map(int, input().split()))
if sum1 > sum2:
    print('Button 1')
elif sum2 > sum1:
    print('Button 2')
else:
    print('Oh no')