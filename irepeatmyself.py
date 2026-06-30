for _ in range(int(input())):
    s = input()

    for i in range(1, len(s) + 1):
        s1 = s[:i] * (len(s) // i)
        s2 = s[:len(s) % i]

        if s1 + s2 == s:
            print(i)
            break