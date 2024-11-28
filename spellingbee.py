s = input()
for _ in range(int(input())):
    w = input()
    if {*w} <= {*s} and len(w) >= 4 and s[0] in w:
        print(w)