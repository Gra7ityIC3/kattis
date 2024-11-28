s = input()
b = s.count('b')
k = s.count('k')
print('boba' if b > k else 'kiki' if k > b else 'boki' if b else 'none')