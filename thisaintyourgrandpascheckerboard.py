n = int(input())
A = [input() for _ in range(n)]
AT = [''.join(col) for col in zip(*A)]
print(any(row.count('B') != n // 2 or 'WWW' in row or 'BBB' in row for row in A + AT) ^ 1)