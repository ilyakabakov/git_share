# Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year: int) -> bool:
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        return True
    else:
        return False


is_year = is_year_leap(int(input('Enter year to check for leap year:')))
print(is_year)
