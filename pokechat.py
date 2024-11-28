s,n=open(0)
print(''.join(s[int(n[i:i+3])-1]for i in range(0,len(n)-1,3)))