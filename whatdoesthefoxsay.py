for _ in range(int(input())):
    sounds = input().split()
    s = set()
    while (line := input()) != 'what does the fox say?':
        s.add(line.split()[2])
    print(' '.join(sound for sound in sounds if sound not in s))