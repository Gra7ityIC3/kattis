minutes, seconds = divmod(int(input()), 60)
hours, minutes = divmod(minutes, 60)
print(f'{hours} : {minutes} : {seconds}')