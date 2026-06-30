best_time = 0
pub = ''
for _ in range(int(input())):
    p, k, t = input().split()
    time = (int(k) + 1) * int(t)
    if time > best_time:
        best_time = time
        pub = p
print(pub, best_time)