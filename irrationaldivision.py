p, q = map(int, input().split())
print(p % 2 * (q % 2 or 2 * (p < q)))