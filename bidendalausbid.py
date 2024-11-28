h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))
print(((h2 - h1) * 60 + m2 - m1) % 1440)