line = input().split()
if sum('ae' in word for word in line) / len(line) >= 0.4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')