for _ in range(int(input())):
    s = {*'abcdefghijklmnopqrstuvwxyz'} - {*input().lower()}
    print(f"missing {''.join(sorted(s))}" if s else 'pangram')