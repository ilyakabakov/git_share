# Простейшие арифметические операции (1)
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть
# произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на
# второе). В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(num1: int, num2: int, operator: str):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Неизвестная операция"


a = arithmetic(
    int(input('Enter the 1st number:')),
    int(input('Enter the 2nd number:')),
    str(input('what operation do you want to calculate:'))
)
print(a)
