# Времена года (4)
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).

# 1
def season(month: int):
    if month in (1, 2, 12):
        return 'Зима'
    elif month in (3, 4, 5):
        return 'Весна'
    elif month in (6, 7, 8):
        return 'Лето'
    elif month in (9, 10, 11):
        return 'Осень'
    else:
        return 'Что-то пошло не так. Введите от 1 до 12'


s = season(int(input('Введите номер месяца:')))
print(s)


# 2

def season2(month2):
    if month2 in range(1, 13):
        return ('Winter', 'Spring', 'Summer', 'Autumn')[((month2) // 3) % 4]
    else:
        print('You entered not right number of month!')


s2 = season2(int(input('Enter the number of month:')))
print(s2)
