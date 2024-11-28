while n := int(input()):
    pile1 = pile2 = 0
    for _ in range(n):
        op, m = input().split()
        m = int(m)
        if op == 'DROP':
            pile2 += m
            print('DROP 2', m)
        else:
            if pile1 >= m:
                pile1 -= m
                print('TAKE 1', m)
            else:
                if pile1: print('TAKE 1', pile1)
                print('MOVE 2->1', pile2)
                print('TAKE 1', m - pile1)
                pile1 = pile2 - m + pile1
                pile2 = 0
    print()