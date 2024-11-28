s = [c.lower() for c in input() if c.isalpha()]
for i in range(len(s)):
    if any(s[i:j] == s[i:j][::-1] for j in range(i + 2, len(s) + 1)):
        print('Palindrome')
        break
else:
    print('Anti-palindrome')