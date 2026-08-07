y = int(input())

def is_leapYear(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True

print(str(is_leapYear(y)).lower())