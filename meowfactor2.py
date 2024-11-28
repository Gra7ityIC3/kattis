import re

S = input()
print(next((i for i, P in enumerate(('meow',
                                     'moew|meo|eow|me.?o?w|m.?ow',
                                     'me|eo|ow|m.?o|m.?.?w|e.?w',
                                     'm|e|o|w')) if re.search(P, S)), 4))