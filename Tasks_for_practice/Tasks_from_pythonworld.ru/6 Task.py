# Простые числа (6)
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое,
# и False - иначе.

def is_prime(num: int):
    if 0 < num < 1000:
        if num % 2 == 0 and num != 2 or num == 1 or num == 0:
            return False
        else:
            return True
    else:
        print('введите число от 0 до 1000')


i = is_prime(int(input('Введите число от 0 до 1000:')))
print(i)
