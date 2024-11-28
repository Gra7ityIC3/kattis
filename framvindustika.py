p, w = map(int, input().split())
hashtags = p * w // 100
dashes = w - hashtags
print(f"[{'#' * hashtags}{'-' * dashes}] | {p:>3}%")