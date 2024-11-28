while n := int(input()):
    boxes = [0] * n
    for i in range(n):
        x1, y1, x2, y2, size = input().split()
        boxes[i] = (float(x1), float(y1), float(x2), float(y2), size)
    for _ in range(int(input())):
        x, y, size = input().split()
        x, y = float(x), float(y)
        for x1, y1, x2, y2, box_size in boxes:
            if x1 <= x <= x2 and y1 <= y <= y2:
                print(size, 'correct' if size == box_size else box_size)
                break
        else:
            print(size, 'floor')
    print()