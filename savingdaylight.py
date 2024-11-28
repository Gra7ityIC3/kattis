for line in open(0):
    date, start, end = line.rsplit(' ', 2)
    h1, m1 = map(int, start.split(':'))
    h2, m2 = map(int, end.split(':'))
    h, m = divmod((h2 - h1) * 60 + m2 - m1, 60)
    print(f'{date} {h} hours {m} minutes')