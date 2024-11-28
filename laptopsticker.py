wc, hc, ws, hs = map(int, input().split())
print(+(wc - ws > 1 and hc - hs > 1))