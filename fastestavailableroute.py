h, w, s = map(int, input().split())
print(f"Your destination will arrive in {sum(input().count('.') for _ in range(h)) * s + s} meters")