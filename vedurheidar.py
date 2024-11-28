v = int(input())
for _ in range(int(input())):
    s, k = input().split()
    print(s, 'opin' if v <= int(k) else 'lokud')