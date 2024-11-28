for _ in range(int(input())):
    name, pss, dob, courses = input().split()
    if int(pss[:4]) >= 2010 or int(dob[:4]) >= 1991:
        print(name, 'eligible')
    elif int(courses) > 40:
        print(name, 'ineligible')
    else:
        print(name, 'coach petitions')