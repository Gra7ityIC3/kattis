n = int(input())
has = [0] * n
wants = [0] * n
for i in range(n):
    _, has[i], wants[i] = input().split()
max_cycle = 0
for i in range(n):
    stop, curr = has[i], wants[i]
    cycle = 1
    while curr != stop:
        try:
            curr = wants[has.index(curr)]
            cycle += 1
        except:
            break
    else:
        max_cycle = max(max_cycle, cycle)
print(max_cycle if max_cycle else 'No trades possible')