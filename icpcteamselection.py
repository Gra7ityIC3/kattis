for _ in range(int(input())):
    n = int(input())
    p = sorted(map(int, input().split()))
    print(sum(p[-2::-2][:n]))