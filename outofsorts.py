def binary_search(x):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == x:
            return True
        elif A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

n, m, a, c, x0 = map(int, input().split())
A = [x0 := (a * x0 + c) % m for _ in range(n)]
print(sum(map(binary_search, A)))