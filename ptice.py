n = int(input())
s = input()
a = [0, 0, 0]
for i in range(n):
    a[0] += s[i] == 'ABC'[i % 3]
    a[1] += s[i] == 'BABC'[i % 4]
    a[2] += s[i] == 'CCAABB'[i % 6]
print(m := max(a))
if a[0] == m: print('Adrian')
if a[1] == m: print('Bruno')
if a[2] == m: print('Goran')