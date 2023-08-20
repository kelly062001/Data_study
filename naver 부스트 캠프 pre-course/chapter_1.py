born_year = int(input())

age = born_year-2023+1

if age<=26 and 20>=age:
    print('대학생')
elif age<20 and 17>=age:
    print('고등학생')
elif age<17 and 14>=age:
    print('중학생')
else:
    print('초등학생')
