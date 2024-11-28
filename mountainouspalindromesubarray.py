n, *x = map(int, open(0))
longest = -1
for i in range(1, n - 1):
    offset = 1
    while True:
        ihi = i + offset
        ilo = i - offset
        if ihi >= n or ilo < 0 or x[ihi] != x[ilo] or x[ilo] >= x[ilo + 1]: break
        offset += 1
    count = 2 * offset - 1
    if count > 2 and count > longest: longest = count
print(longest)