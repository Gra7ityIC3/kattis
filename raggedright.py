n = max(a := [*map(len, open(0))])
a.pop()
print(sum((n - m) ** 2 for m in a))